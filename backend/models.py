from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    admin  = Column(Boolean)