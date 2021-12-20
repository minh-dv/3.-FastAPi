from sqlalchemy import Column, String, Integer
from db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    mail = Column(String(255), nullable=False, comment="Gmail Account")
    password = Column(String(255), nullable=False, comment="Password")
