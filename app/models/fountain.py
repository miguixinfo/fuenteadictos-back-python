from sqlalchemy import Column, String, LargeBinary, Boolean, Integer, Float
from sqlalchemy.orm import relationship
from models.base_object import BaseObject

class Fountain(BaseObject):
    __tablename__='fountain'
    
    name = Column(String(20), unique=True, index=True, nullable=False)
    description = Column(String(255), nullable=False)
    image = Column(LargeBinary, nullable=False)
    operative = Column(Boolean,  index=True, nullable=False)
    average_points = Column(Integer, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    
    
    reviews = relationship("Review", back_populates="fountain")
    warnings = relationship("Warning", back_populates="fountain")
    
    