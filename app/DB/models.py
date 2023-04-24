from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: str
    user_type: Optional[str] = None

class UserCreate(UserBase):
    password: str
    confirm_password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
