from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    admin  = Column(Boolean)
    
class Sapling_tray(Base):
    __tablename__ = 'sapling_tray'
    
    id = Column(Integer, primary_key=True, index=True)
    create_date = Column(DateTime, default=datetime.today().strftime('%Y-%m-%d'))
    origin_id = Column(String)
    propagation_lot_id = Column(String)
    x_pos = Column(Integer)
    y_pos = Column(Integer)
    row_num = Column(Integer)
    col_num = Column(Integer)
    
    # * Foreign Keys  * #
    species_id = Column(Integer, ForeignKey('species.id'))
    propagation_method_id = Column(Integer, ForeignKey('propagation_method.id'))
    room_id = Column(Integer, ForeignKey('room.id'))

    species = relationship("Species", back_populates='sapling_tray')
    propagation_method = relationship("Propagation_method", back_populates='sapling_tray')
    room = relationship("Room", back_populates='sapling_tray')
    

class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
    sapling_tray = relationship("Sapling_tray", back_populates='species')
    
class Propagation_method(Base):
    __tablename__ = 'propagation_method'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
    sapling_tray = relationship("Sapling_tray", back_populates='propagation_method')
    
class Room(Base):
    __tablename__ = 'room'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
    sapling_tray = relationship("Sapling_tray", back_populates='room')
    