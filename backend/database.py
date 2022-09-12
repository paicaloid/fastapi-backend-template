from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import Settings

settings = Settings()

DB_USR = settings.DB_USR
DB_PWD = settings.DB_PWD
DB_IP = settings.DB_IP
DB_PORT = settings.DB_PORT
DB_SCHEMA = settings.DB_SCHEME


SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USR}:{DB_PWD}@{DB_IP}:{DB_PORT}/{DB_SCHEMA}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

