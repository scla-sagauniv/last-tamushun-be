from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class MediaCreate(BaseModel):
    image_url: Optional[str] = None
    movie_url: Optional[str] = None
    lat: Optional[str] = None
    lon: Optional[str] = None

class MediaUpdate(BaseModel):
    image_url: Optional[str] = None
    movie_url: Optional[str] = None
    lat: Optional[str] = None
    lon: Optional[str] = None

class MediaResponse(BaseModel):
    id: int
    userid: Optional[int] = None
    image_url: Optional[str] = None
    movie_url: Optional[str] = None
    lat: Optional[str] = None
    lon: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class MediaList(BaseModel):
    medium: List[MediaResponse]
    
    class Config:
        orm_mode = True