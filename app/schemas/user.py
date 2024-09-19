from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime
import re


class UserResponse(BaseModel):
    uuid: str
    email: str
    username: str
    created_date: datetime
    voided: bool
    
    class Config:
        orm_mode = True
        
        
class UserCreate(BaseModel):
    email: EmailStr = Field(..., description="El email del usuario")
    username: str = Field(..., min_length=1, max_length=20, description="El nombre de usuario")
    password: str = Field(..., min_length=1, max_length=255, description="La contraseña del usuario")
    
    @field_validator('username')
    def validate_username(cls, value):
        if not value.isalnum():
            raise ValueError('El nombre de usuario solo puede contener letras y números')
        return value
    
    @field_validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres')
        if not re.search(r'[A-Z]', value):
            raise ValueError('La contraseña debe contener al menos una letra mayúscula')
        if not re.search(r'[a-z]', value):
            raise ValueError('La contraseña debe contener al menos una letra minúscula')
        if not re.search(r'[0-9]', value):
            raise ValueError('La contraseña debe contener al menos un dígito')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError('La contraseña debe contener al menos un carácter especial')
        return value
    
