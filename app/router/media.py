from fastapi import APIRouter

router = APIRouter()

# media一覧取得
@router.get("/media")
async def list_media():
    pass

# create
@router.post("/media")
async def create_media():
    pass

# update
@router.patch("/media/{media_id}")
async def update_media():
    pass

# delete
@router.delete("/media/{media_id}")
async def delete_media():
    pass