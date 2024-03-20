from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class MediaCreate(BaseModel):
    image_url: Optional[str] = None
    movie_url: Optional[str] = None
    lat: Optional[int] = None
    lon: Optional[int] = None

class MediaUpdate(BaseModel):
    image_url: Optional[str] = None
    movie_url: Optional[str] = None
    lat: Optional[int] = None
    lon: Optional[int] = None

class MediaResponse(BaseModel):
    id: int
    user_id: Optional[int] = None
    image_url: Optional[str] = None
    movie_url: Optional[str] = None
    lat: Optional[int] = None
    lon: Optional[int] = None
    created_at: datetime = None
    updated_at: datetime = None

class MediaList(BaseModel):
    medium: List[MediaResponse]
    
    class Config:
        orm_mode = True