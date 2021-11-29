from fastapi import APIRouter
from pydantic.errors import EmailError
from config.database import conn
from models.user import users
from schemas.index import User
import uuid

user = APIRouter()

# Create a get that will pull user data
@user.get("/")
async def getAll_Users():
  return conn.execute(users.select()).fetchall()

# Pull user data by id value
@user.get("/{id}")
async def get_user(id:str):
  return conn.execute(users.select().where(users.c.id == id)).fetchall()

# write user data
@user.post("/")
async def create_user(user: User):
  return conn.execute(users.insert().values(
    id=uuid.uuid1(),
    username=user.username,
    firstName=user.firstName,
    lastName=user.lastName,
    email=user.email,
    password=user.password,
  )).fetchall()

# Update user data
@user.put("/{id}")
async def update_user(id:str,user: User):
  conn.execute(users.update().values(
    username=user.username,
    firstName=user.firstName,
    lastName=user.lastName,
    email=user.email,
    password=user.password,
  )).where(users.c.id == id)
  return conn.execute(users.select()).fetchall()

# Delete user
@user.get("/{id}")
async def delete_user(id:str):
  conn.execute(users.delete().where(users.c.id == id))
  return conn.execute(users.select()).fetchall()

