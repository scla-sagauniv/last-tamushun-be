from fastapi import APIRouter, Depends, HTTPException, Header
import jwt
from sqlalchemy.orm import Session

from app.db import get_db
from app.schema.media import MediaCreate, MediaList, MediaResponse, MediaUpdate
from app.models.media import Media as DBMedia
router = APIRouter()

# jwt検証用
async def get_user_id(authorization: str = Header(...)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise credentials_exception
        payload = jwt.decode(token, options={"verify_signature": False})
        user_id = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        return user_id
    except (ValueError):
        raise credentials_exception
    

# media一覧取得
@router.get("/media", response_model=MediaList)
async def list_media(
    user_id: str = Depends(get_user_id),
    db: Session = Depends(get_db)
):
    media_list = db.query(DBMedia).filter(DBMedia.user_id == user_id).all()
    return media_list

# create
@router.post("/media", response_model=MediaResponse)
async def create_media(media: MediaCreate, user_id: str = Depends(get_user_id), db: Session = Depends(get_db)):
    if media is None:
        raise HTTPException(status_code=400, detail="Bad Request")
    
    db_media = DBMedia(**media.dict(), user_id=user_id)

    if db_media.user_id != user_id:
        raise HTTPException(status_code=403, detail="User is not authorized to create media")
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media

# update
@router.patch("/media/{media_id}", response_model=MediaResponse)
async def update_media(
    media_id: int,
    updated_media: MediaUpdate,
    user_id: str = Depends(get_user_id),
    db: Session = Depends(get_db)
):
    db_media = db.query(DBMedia).filter(DBMedia.id == media_id).first()
    if db_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    if db_media.user_id != user_id:
        raise HTTPException(status_code=403, detail="User is not authorized to update this media")

    if updated_media.image_url:
        db_media.image_url = updated_media.image_url
    if updated_media.movie_url:
        db_media.movie_url = updated_media.movie_url
    if updated_media.lat:
        db_media.lat = updated_media.lat
    if updated_media.lon:
        db_media.lon = updated_media.lon 
    db.commit()
    db.refresh(db_media)
    return db_media

# delete
@router.delete("/media/{media_id}")
async def delete_media(media_id: int, user_id: str = Depends(get_user_id), db: Session = Depends(get_db)):
    db_media = db.query(DBMedia).filter(DBMedia.id == media_id).first()
    if db_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    if db_media.user_id != user_id:
        raise HTTPException(status_code=403, detail="User is not authorized to delete this media")

    db.delete(db_media)
    db.commit()
    return {"message": "deleted successfully"}