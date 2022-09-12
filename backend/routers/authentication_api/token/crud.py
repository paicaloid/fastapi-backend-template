from datetime import datetime, timedelta
from fastapi import HTTPException
from jose import jwt
from sqlalchemy.orm import Session
from typing import Optional

from .... import models
from ....dependencies import pwd_context, SECRET_KEY, ALGORITHM

def get_user_by_username(db : Session, username : str):
    return db.query(models.User).filter(models.User.username == username).first()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db, username: str, password: str):
    db_user = get_user_by_username(db=db, username=username)
    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail=f"username : {username} not found"
        )
        
    if not verify_password(plain_password=password, hashed_password=db_user.password):
        raise HTTPException(
            status_code=401,
            detail=f"Incorrect password"
        )
    return db_user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt