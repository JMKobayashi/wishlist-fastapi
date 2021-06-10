from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    name = Column(String, index=True)
    description = Column(String)
    link = Column(String)
    user_have = Column(Boolean, default=False)
    owner_id = Column(Integer,  ForeignKey("users.id"))

    owner = relationship("Users", back_populates="items")

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)

    items = relationship("Item", back_populates="owner")
