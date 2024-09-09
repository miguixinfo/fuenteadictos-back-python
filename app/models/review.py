from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_object import BaseObject

class Review(BaseObject):
    __tablename__='review'
    
    header = Column(String(255))
    description = Column(String(500))
    jet_points = Column(Integer)
    cold_points = Column(Integer)
    pretty_points = Column(Integer)
    flavor_points = Column(Integer)
    
    user_id = Column(Integer, ForeignKey("user.id"))
    fountain_id = Column(Integer, ForeignKey("fountain.id"))
    
    user = relationship("User", back_populates="reviews")
    fountain = relationship("Fountain", back_populates="reviews")