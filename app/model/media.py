from sqlalchemy import Column, Integer, String, ForeignKey

from app.db import Base

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    image_url = Column(String(255))
    movie_url = Column(String(255))
    lat = Column(Integer)
    lon = Column(Integer)

