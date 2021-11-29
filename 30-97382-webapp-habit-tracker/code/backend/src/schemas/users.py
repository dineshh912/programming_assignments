from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Users

# Creating new user
UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)

# Retriving specific user information
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)

# Retrving user information inside application
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)