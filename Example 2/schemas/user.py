from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    name: Optional[str]
    mail: Optional[str]

    class Config:
        orm_mode = True


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: str


# Properties to receive on item creation
class UserCreate(UserBase):
    password: Optional[str]


# Properties to receive on item update
class UserUpdate(UserBase):
    password: Optional[str]


# Properties to return to client
class User(UserInDBBase):
    pass


# Properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


class UserAuth(BaseModel):
    mail: Optional[str]
    password: Optional[str]



