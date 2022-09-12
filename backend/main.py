from fastapi import APIRouter, FastAPI

from . import models
from .database import engine, SessionLocal

from .routers.authentication_api.authenticate import authenticate
from .routers.authentication_api.token import token
from .routers.authentication_api.user import user

models.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {"name": 'Authentication', "description": "Authentication related endpoints"},
]

router = APIRouter()
app = FastAPI()

router.include_router(authenticate.router)
router.include_router(token.router)
router.include_router(user.router)



app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}