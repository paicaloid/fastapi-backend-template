from fastapi import HTTPException
from sqlalchemy.orm import Session

from .... import models
from ....dependencies import pwd_context
from ....schemas.auth import UserCreate, UserUpdate

def get_user_by_username(db : Session, username : str):
    return db.query(models.User).filter(models.User.username == username).first()

def check_username(db, username):
    db = get_user_by_username(db=db, username=username)
    if db:
        raise HTTPException(
            status_code=400,
            detail=f"username : {username}, algety registered"
        )
    return db

def create_user(db : Session, user : UserCreate):
    _ = check_username(db=db, username=user.username)
    hashed_pwd = pwd_context.hash(user.password)
    db_user = models.User(
        username=user.username,
        password=hashed_pwd,
        admin=user.admin
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_list(db : Session):
    return db.query(models.User).all()

def get_user_by_id(db : Session, user_id : int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db : Session, username : str):
    return db.query(models.User).filter(models.User.username == username).first()

def update_user(db : Session,user_id:int,user: UserUpdate):
    hashed_pwd = pwd_context.hash(user.password)
    user.password = hashed_pwd
    db_user = db.query(models.User).filter(
        models.User.id == user_id
        )
    if not db_user:
        raise HTTPException(status_code=404, detail="user_id not found")
    try:
        db_user.update(user.dict(exclude_unset=True))
        db.commit()
    except:
        raise HTTPException(status_code=500, detail="Cannot update user")
    return db_user.first()