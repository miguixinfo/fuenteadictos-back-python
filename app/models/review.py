from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_object import BaseObject

class Review(BaseObject):
    __tablename__='review'
    
    header = Column(String(255)) # Título de la reseña
    description = Column(String(500)) # Descripción de la reseña
    jet_points = Column(Integer) # Puntos de chorro
    cold_points = Column(Integer) # Puntos de frio
    pretty_points = Column(Integer) # Puntos de belleza
    flavor_points = Column(Integer) # Puntos de sabor
    
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    fountain_id = Column(Integer, ForeignKey("fountain.id"), nullable=False)
    
    user = relationship("User", back_populates="reviews")
    fountain = relationship("Fountain", back_populates="reviews")