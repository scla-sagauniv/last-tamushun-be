from fastapi import APIRouter

router = APIRouter()

# ユーザー新規登録
@router.post("/signup")
async def Signup():
    pass

# ユーザーログイン
@router.post("/login")
async def Login():
    pass

# ユーザー情報取得
@router.get("/user/{userid}")
async def userinfo():
    pass

# ユーザー情報アップデート
@router.patch("/user/{userid}")
async def update_user():
    pass
