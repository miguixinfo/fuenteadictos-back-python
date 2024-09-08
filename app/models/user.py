
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.sql import func
from models.base_object import BaseObject
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from db.base import Base

class User(BaseObject):
    __tablename__= 'user'
    
    email = Column(String(50), unique=True, index=True, nullable=False)
    username = Column(String(20), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)