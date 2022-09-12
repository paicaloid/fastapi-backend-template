from datetime import timedelta
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from . import crud
from ....dependencies import get_db, ACCESS_TOKEN_EXPIRE_MINUTES
from ....schemas.auth import Token

router = APIRouter(
    prefix="/token",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    db_user = crud.authenticate_user(db=db, username=form_data.username, password=form_data.password)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )
    
    return Token(access_token=access_token, token_type="bearer")