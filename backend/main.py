import re
from fastapi import APIRouter, FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models
from .database import engine, SessionLocal

from .dependencies import get_db


from .routers.authentication_api.authenticate import authenticate
from .routers.authentication_api.token import token
from .routers.authentication_api.user import user

models.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {"name": 'Authentication', "description": "Authentication related endpoints"},
]

router = APIRouter()
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router.include_router(authenticate.router)
router.include_router(token.router)
router.include_router(user.router)



app.include_router(router)

from datetime import date,datetime
from typing import List, Optional

from pydantic import BaseModel


class StringBase(BaseModel):
    name:str
    class Config:
        orm_mode = True
        
class String(StringBase):
    id:int

class Sapling_trayBase(BaseModel):
    create_date: date
    origin_id:str
    propagation_lot_id:str
    x_pos:Optional[int] = 0
    y_pos:Optional[int] = 0

    class Config:
        orm_mode = True
        
class Sapling_trayCreate(Sapling_trayBase):
    species_id:int
    propagation_method_id:int
    room_id:int
    row_num:int
    col_num:int

class Sapling_tray(Sapling_trayBase):
    id:int
    species: String
    propagation_method: String
    room: String

    class Config:
        orm_mode = True
        
class Sapling_trayNrm(Sapling_trayBase):
    id:int
    species_id:int
    propagation_method_id: int
    room_id:int


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/", response_model=Sapling_tray)
def create_item(data : Sapling_trayCreate, db : Session = Depends(get_db)):
    db_item = models.Sapling_tray(**data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    return db_item

@app.get("/query/")
def query_item(db : Session = Depends(get_db)):
    return db.query(models.Sapling_tray).all()

@app.get("/items/{item_id}", response_model=Sapling_tray)
def read_item(item_id: int, db : Session = Depends(get_db)):
    return db.query(models.Sapling_tray).filter(
        models.Sapling_tray.id == item_id).first()
    
@app.get("/items_non/{item_id}", response_model=Sapling_trayNrm)
def read_item(item_id: int, db : Session = Depends(get_db)):
    return db.query(models.Sapling_tray).filter(
        models.Sapling_tray.id == item_id).first()