from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Mentalhealth

# Creating new mental health entry
MentalhealthInSchema = pydantic_model_creator(
    Mentalhealth, name="MentalhealthIn", exclude=["added_by_id"], exclude_readonly=True)

# Retriving mental health details
MentalhealthOutSchema = pydantic_model_creator(
    Mentalhealth, name="Mentalhealth", exclude =[
      "modified_at", "added_by_id.password", "added_by_id.created_at", "added_by_id.modified_at"
    ]
)


class UpdateMentalhealth(BaseModel):
    title: Optional[str]
    notes: Optional[str]