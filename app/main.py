from typing import Union
from app.db import get_db
from app.router import user,media
from fastapi import FastAPI

app = FastAPI()

app.include_router(user.router)
app.include_router(media.router)