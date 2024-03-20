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
    user_id: int = Depends(get_user_id),
    db: Session = Depends(get_db)
):
    media_list = db.query(DBMedia).filter(DBMedia.user_id == user_id).all()

    media_response_list = []
    for media in media_list:
        media_response = MediaResponse(
            id=media.id,
            user_id=media.user_id,
            image_url=media.image_url,
            movie_url=media.movie_url,
            lat=media.lat,
            lon=media.lon,
            created_at=media.created_at,
            updated_at=media.updated_at
        )
        media_response_list.append(media_response)
    return MediaList(medium=media_response_list)

# create
@router.post("/media",response_model=MediaResponse)
async def create_media(media: MediaCreate, user_id: int = Depends(get_user_id), db: Session = Depends(get_db)):
    if media is None:
        raise HTTPException(status_code=400, detail="Bad Request")
    
    db_media = DBMedia(**media.dict(), user_id=user_id)

    if db_media.user_id != user_id:
        raise HTTPException(status_code=403, detail="User is not authorized to create media")
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return MediaResponse(
        id=db_media.id,
        user_id=db_media.user_id,
        image_url=db_media.image_url,
        movie_url=db_media.movie_url,
        lat=db_media.lat,
        lon=db_media.lon,
        created_at=db_media.created_at,
        updated_at=db_media.updated_at
    )

# update
@router.patch("/media/{media_id}", response_model=MediaResponse)
async def update_media(
    media_id: int,
    updated_media: MediaUpdate,
    user_id: int = Depends(get_user_id),
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
    return MediaResponse(
        id=db_media.id,
        user_id=db_media.user_id,
        image_url=db_media.image_url,
        movie_url=db_media.movie_url,
        lat=db_media.lat,
        lon=db_media.lon,
        created_at=db_media.created_at,
        updated_at=db_media.updated_at
    )

# delete
@router.delete("/media/{media_id}")
async def delete_media(media_id: int, user_id: int = Depends(get_user_id), db: Session = Depends(get_db)):
    db_media = db.query(DBMedia).filter(DBMedia.id == media_id).first()
    if db_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    if db_media.user_id != user_id:
        raise HTTPException(status_code=403, detail="User is not authorized to delete this media")

    db.delete(db_media)
    db.commit()
    return {"message": "deleted successfully"}