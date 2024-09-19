from sqlalchemy import Column, String, LargeBinary, Boolean, Integer, Numeric
from sqlalchemy.orm import relationship
from models.base_object import BaseObject

class Fountain(BaseObject):
    __tablename__='fountain'
    
    name = Column(String(20), unique=True, index=True, nullable=False)
    description = Column(String(255), nullable=False)
    # Si la aplicación escala bien, podemos cambiar la imagen
    # de large binary a un string y guardar image_url
    # la imagen, por rendimiento estará almacenada en un AWS S3 o similar
    image = Column(LargeBinary, nullable=False)
    operative = Column(Boolean,  index=True, nullable=False)
    # puede causar problemas a la hora de calcular el punto medio, valorar si es mejor calcularlo al vuelo
    average_points = Column(Integer, index=True)
    latitude = Column(Numeric(10, 6), nullable=False)
    longitude = Column(Numeric(10, 6), nullable=False)
    
    
    reviews = relationship("Review", back_populates="fountain")
    warnings = relationship("Warning", back_populates="fountain")
    
    