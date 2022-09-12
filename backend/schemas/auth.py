from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username : str
    admin : bool
    
class UserCreate(UserBase):
    password : str
    
class UserUpdate(BaseModel):
    password : Optional[str]
    admin : Optional[bool]
    
class User(UserBase):
    id : int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
    expired_date : Optional[datetime]
    
class TokenGet(BaseModel):
    access_token: str
    
class TokenData(BaseModel):
    username: Optional[str] = None

class Login(BaseModel):
    username: str
    password: str