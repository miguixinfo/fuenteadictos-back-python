from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any
from schemas.fountain import FountainSmallResponse
from schemas.user import UserSmallResponse

class WarningResponse(BaseModel):
    uuid: str
    operative: bool
    fountain: FountainSmallResponse
    user: UserSmallResponse
    
    class Config:
        orm_mode = True
        
        
class WarningCreate(BaseModel):
    operative: bool = Field(..., description="Si la advertencia es operativa")
    fountain_uuid: str = Field(..., description="El uuid de la fuente")
    user_uuid: str = Field(..., description="El uuid del usuario")
