from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

from . import crud
from ....dependencies import get_db
from ....schemas.auth import User, UserCreate, UserUpdate

router = APIRouter(
    prefix="/user",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=User)
def create_user(user : UserCreate, db : Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/", response_model=List[User])
def get_user_list(db: Session = Depends(get_db)):
    return crud.get_user_list(db=db)

@router.get("/{user_id}", response_model=User)
# @router.get("/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(db=db, user_id=user_id)

@router.get("/username/{username}", response_model=User)
def get_user_by_username(username: str ,db: Session = Depends(get_db)):
    return crud.get_user_by_username(db=db, username=username)

@router.patch("/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate,db : Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, user=user) 