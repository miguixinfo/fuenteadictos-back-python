from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any
from schemas.fountain import FountainSmallResponse
from schemas.user import UserSmallResponse

class ReviewResponse(BaseModel):
    uuid: str
    header: str
    description: str
    jet_points: int
    cold_points: int
    pretty_points: int
    flavor_points: int
    user: UserSmallResponse
    fountain: FountainSmallResponse
    
    class Config:
        orm_mode = True
        
        
class ReviewCreate(BaseModel):
    header: str = Field(..., min_length=1, max_length=25, description="El título de la reseña")
    description: str = Field(..., min_length=1, max_length=500, description="La descripción de la reseña")
    jet_points: int = Field(..., ge=1, le=5, description="Puntos de chorro")
    cold_points: int = Field(..., ge=1, le=5, description="Puntos de frio")
    pretty_points: int = Field(..., ge=1, le=5, description="Puntos de belleza")
    flavor_points: int = Field(..., ge=1, le=5, description="Puntos de sabor")
    user_uuid: str = Field(..., description="El uuid del usuario")
    fountain_uuid: str = Field(..., description="El uuid de la fuente")