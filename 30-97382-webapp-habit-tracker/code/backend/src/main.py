from fastapi import FastAPI # fastapi library
from fastapi.middleware.cors import CORSMiddleware # Handling cors

# Imports related to database and ORM Mapper
from tortoise import Tortoise
from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

# Enablbe schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

# Importing  routes
from src.routes import users, mentalhealth


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# adding routes
app.include_router(users.router)
app.include_router(mentalhealth.router)

# Registering Database
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)
