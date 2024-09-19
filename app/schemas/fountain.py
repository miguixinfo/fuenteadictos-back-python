from pydantic import BaseModel, Field,field_validator
from datetime import datetime
from typing import Optional
import re

class FountainResponse(BaseModel):
    uuid: str
    name: str
    description: str
    created_date: datetime
    operative: bool
    average_points: Optional[int]
    latitude: float
    longitude: float
    
    class Config:
        orm_mode = True
        
        
class FountainCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=20, description="El nombre de la fuente")
    description: str = Field(..., min_length=1, max_length=255, description="Una descripción de la fuente")
    image: bytes = Field(..., description="La imagen de la fuente")
    operative: bool = Field(True, description="Si la fuente está operativa")
    latitude: float = Field(..., ge=-90, le=90, description="La latitud de la fuente")
    longitude: float = Field(..., ge=-180, le=180, description="La longitud de la fuente")

    @field_validator('latitude')
    def validate_latitude(cls, value):
        if not (-90 <= value <= 90):
            raise ValueError('La latitud debe estar entre -90 y 90')
        return value

    @field_validator('longitude')
    def validate_longitude(cls, value):
        if not (-180 <= value <= 180):
            raise ValueError('La longitud debe estar entre -180 y 180')
        return value