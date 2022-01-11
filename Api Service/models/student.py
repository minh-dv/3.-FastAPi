from sqlalchemy import Column, String

from db.base import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(String(7), primary_key=True)
    name = Column(String(50))
    class_name = Column(String(50))
