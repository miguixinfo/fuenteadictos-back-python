from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any
from schemas.fountain import FountainResponse
from schemas.user import UserResponse

class WarningResponse(BaseModel):
    uuid: str
    operative: bool
    fountain: FountainResponse
    user: UserResponse
    
    class Config:
        orm_mode = True
        
        
class WarningCreate(BaseModel):
    operative: bool = Field(True, description="Si la advertencia es operativa")
    fountain_uuid: str = Field(..., description="El uuid de la fuente")
    user_uuid: str = Field(..., description="El uuid del usuario")
