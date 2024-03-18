from fastapi import APIRouter

router = APIRouter()


@router.post("/signup")
async def Signup():
    pass

@router.post("/login")
async def Login():
    pass

@router.get("/user/{userid}")
async def userinfo():
    pass

@router.patch("/user/{userid}")
async def update_user():
    pass
