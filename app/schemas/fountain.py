from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

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
    name: str
    description: str
    image: bytes
    operative: bool
    latitude: float
    longitude: float