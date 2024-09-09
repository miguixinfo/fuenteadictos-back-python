
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_object import BaseObject
from db.base import Base

class User(BaseObject):
    __tablename__= 'user'
    
    email = Column(String(50), unique=True, index=True, nullable=False)
    username = Column(String(20), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    
    reviews = relationship("Review", back_populates="user")
    warnings = relationship("Warning", back_populates="user")