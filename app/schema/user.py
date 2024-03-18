from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    hashed_password: Optional[str] = None

class UserLogin(BaseModel):
    email: Optional[EmailStr] = None
    hashed_password: Optional[str] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    hashed_password: Optional[str] = None

class UserToken(BaseModel):
    token: str

class UserResponse(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True