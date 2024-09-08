from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    
class UserResponse(BaseModel):
    uuid: str
    email: str
    username: str
    created_date: datetime
    voided: bool
    
    class Config:
        orm_mode = True