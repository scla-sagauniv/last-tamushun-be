from fastapi import APIRouter

router = APIRouter()


@router.get("/user/{userid}")
async def userinfo():
    pass
