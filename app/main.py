from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/", response_model = List[schemas.Item], tags = ["Items"])
def read_items(db: Session = Depends(get_db)):
    """Retrieve all items
    Return:
        {
            "name": <String> - Item name,
            "description": <String> - Item description,
            "link": <String> - Item link,
            "user_have": <Boolean>,
            "owner": "User ID",
            "id": "Item ID"
        }
    """
    # Call function to retrieve all the items in the database
    return crud.get_items(db)

@app.get("/item/{user_id}/random/", response_model = schemas.Item, tags = ["Items"])
def read_random_item(user_id: int, db: Session = Depends(get_db)):
    """Retrieve random item from a specific user
    Return:
        {
            "name": <String>"Item name",
            "description": <String>"Item description",
            "link": <String>"Item link",
            "user_have": <Boolean>,
            "owner": <Integer> - User ID,
            "id": <Integer> - Item ID
        }
    Parameters:
        {user_id}: "Owner ID"
    """
    # Call function to retrieve a random item of a given user
    return crud.get_random_item(user_id, db)

@app.put("/item/{user_id}/got/", response_model = schemas.Item, tags = ["Items"])
def update_user_has_item(user_id: int, item: schemas.UserGotItem, db: Session = Depends(get_db)):
    """Update the status user_have of an item from a specific user
    Return:
        {
            "name": <String>"Item name",
            "description": <String>"Item description",
            "link": <String>"Item link",
            "user_have": <Boolean>,
            "owner": <Integer> - User ID,
            "id": <Integer> - Item ID
        }
    Parameters:
        {user_id}: <Integer> - Owner ID
        {
            "name": <String> - Name of the item,
            "user_have": <Boolean>
        }
    """
    # Call function to update status of user_have
    return crud.update_user_got_item(db, item, user_id)

@app.post("/item/{user_id}/user/", response_model = schemas.Item, tags = ["Items"])
def create_item(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """Create an item
    Return:
        {
            "name": <String> - Item name,
            "description": <String> - Item description,
            "link": <String> - Item link,
            "user_have": <Boolean>,
            "owner": <Integer> - User ID,
            "id": <Integer> - Item ID
        }
    Parameters:
        {user_id}: <Integer> - Owner ID
        {
            "name": <String> - Item name,
            "description": <String> - Item description,
            "link": <String> - Item link,
            "user_have": <Boolean>
        }
    """
    # Call function to create an Item
    return crud.create_user_item(db, item, user_id)

@app.get("/users/", response_model = List[schemas.Users], tags = ["User"])
def read_users(db: Session = Depends(get_db)):
    """Retrieve all Users
    Return:
        {
            "email": <String> - User email,
            "name": <String> - User name,
            "id": <Integer> - User ID
        }
    """
    # Call function to retrieve all the items in the database
    return crud.get_users(db)

@app.post("/user/", response_model = schemas.User, tags = ["User"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Create an User
    Return:
        {
            "email": <String> - User email,
            "name": <String> - User name,
            "id": <Integer> - User ID,
            "Items": <List> - Items in the wishlist
        }
    Parameters:
        {
            "email": <String> - User email,
            "name": <String> - User name,
            "password": <String> - User password
        }
    """
    # Verify if the email is already registered
    db_user = crud.get_user_email(db, user.email)
    # If the email is already in the Database
    if db_user:
        # Raise an Exception indicating that the email is already registered
        raise HTTPException(status_code=400, detail="Email already registered")
    # If the email is not in the Database
    # Call the function to create new user
    return crud.create_user(db, user)

@app.get("/user/{user_id}", response_model = schemas.User, tags = ["User"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    """Retrieve details of a specific User
    Return:
        {
            "email": <String> - User email,
            "name": <String> - User name,
            "id": <Integer> - User ID,
            "Items": <List> - Items in the wishlist
        }
    Parameters:
        {user_id}: <Integer> - Owner ID
    """
    # Call function to retrieve the details of a given User
    return crud.get_user(db, user_id)