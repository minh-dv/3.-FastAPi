from typing import Optional, List

from pydantic import BaseModel


# Shared properties
class StudentBase(BaseModel):
    name: Optional[str]
    class_name: Optional[str]


# Properties shared by models stored in DB
class StudentInDBBase(StudentBase):
    id: str

    class Config:
        orm_mode = True


# Properties to receive on item creation
class StudentCreate(StudentInDBBase):
    pass


# Properties to receive on item update
class StudentUpdate(StudentInDBBase):
    pass


# Properties to return to client
class Student(StudentInDBBase):
    pass


# Properties stored in DB
class StudentInDB(StudentInDBBase):
    pass



