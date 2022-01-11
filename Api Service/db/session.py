from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv('DATABASE_URL')

engine = create_engine(database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autoflush=False, autocommit=False,bind=engine)
