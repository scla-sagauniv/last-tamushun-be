from sqlalchemy import Column, Integer, String, DateTime, func

from app.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    hashed_password = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    image_url = Column(String(255))
    movie_url = Column(String(255))
    lat = Column(Integer)
    lon = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
