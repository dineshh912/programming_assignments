from typing import Optional
from pydantic import BaseModel

# user name from the token is strng
class TokenData(BaseModel):
    username: Optional[str] = None

# sending message back to user
class Status(BaseModel):
    message: str