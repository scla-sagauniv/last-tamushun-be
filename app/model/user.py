from sqlalchemy import Column, Integer, String, ForeignKey

from app.db import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    hashed_password = Column(String(255))

