from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from fastapi import HTTPException

from . import models, schemas
"""Function to retrieve all items in the database"""
def get_items(db: Session):
    return db.query(models.Item).all()

"""Function to retrieve a random item from the database"""
def get_random_item(user_id:int, db: Session):
    return db.query(models.Item).filter_by(owner_id=user_id).order_by(func.random()).first()

"""Function to update the status user_have of an item from a specific User"""
def update_user_got_item(db: Session, item_name: schemas.ItemBase, user_id: int):
    try:
        item = db.query(models.Item).filter_by(name = item_name.name, owner_id=user_id).first()
        item.user_has = item_name.user_has
    except AttributeError:
        raise HTTPException(status_code=400, detail="Invalid atribute")

    db.commit()
    return db.query(models.Item).filter_by(name = item_name.name).first()

"""Function to create an Item"""
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    user = db.query(models.Users).filter_by(id=user_id)
    if not user:
        raise HTTPException(status_code = 404, detail="User not found")
    db_item = models.Item(**item.dict(), owner_id = user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

"""Function to retrieve all users in the database"""
def get_users(db: Session):
    return db.query(models.Users).all()

"""Function to retrieve details of a given User"""
def get_user(db: Session, id: int):
    return db.query(models.Users).filter_by(id = id).first()

"""Function to verify if an email is already registered in the database"""
def get_user_email(db: Session, email: str):
    return db.query(models.Users).filter_by(email = email).first()

"""Function to create an User"""
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.Users(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user