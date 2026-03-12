from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str] = None
    phone: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    email: str
    name: Optional[str] = None
    phone: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True