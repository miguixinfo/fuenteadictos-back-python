import uuid
from sqlalchemy import Column, DateTime, Boolean, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.dialects.mysql import CHAR
from db.base import Base

class BaseObject(Base):
    __abstract__ = True # Para indicar que no es una tabla real
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    uuid = Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    voided = Column(Boolean, default=False)