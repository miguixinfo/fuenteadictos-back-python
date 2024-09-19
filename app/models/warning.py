from sqlalchemy import Column, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_object import BaseObject

class Warning(BaseObject):
    __tablename__='warning'
    
    operative = Column(Boolean, nullable=False)
    
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    fountain_id = Column(Integer, ForeignKey("fountain.id"), nullable=False)
    
    user = relationship("User", back_populates="warnings")
    fountain = relationship("Fountain", back_populates="warnings")
    