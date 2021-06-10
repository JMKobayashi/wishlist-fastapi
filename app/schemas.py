from typing import List, Optional

from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = ""
    link: Optional[str] = ""
    user_have: Optional[bool] = False

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    name: str
    description: str
    link: str
    user_have: bool
    owner_id: int

    class Config:
        orm_mode = True

class UserGotItem(BaseModel):
    name: str
    user_have: Optional[bool] = True

class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    password: str

class Users(UserBase):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    name: str
    email: str
    items: List[Item] = []

    class Config:
        orm_mode = True