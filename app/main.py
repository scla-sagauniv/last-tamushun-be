from app.router import user,media
from fastapi import FastAPI

app = FastAPI()

app.include_router(user.router)
app.include_router(media.router)