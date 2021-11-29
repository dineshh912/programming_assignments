from pydantic import BaseModel

class User(BaseModel):
  id:str
  username: str
  firstName: str
  lastName: str
  email: str
  password: str