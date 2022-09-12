from fastapi import Depends, APIRouter, Header
from sqlalchemy.orm import Session
from typing import Union

from . import crud
from ....dependencies import get_db, custom_authorize_and_get_user_by_token
from ....schemas.auth import User

router = APIRouter(
    prefix="/authenticate",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=User)
def auth_token(x_token: Union[str, None] = Header(default=None) , db : Session = Depends(get_db)):
    return custom_authorize_and_get_user_by_token(token=x_token,db=db)