from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.user import User as DBUser
from app.schema.user import UserCreate, UserResponse

router = APIRouter()

# userをポストするだけのサンプル
@router.post("/user/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = DBUser(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

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
