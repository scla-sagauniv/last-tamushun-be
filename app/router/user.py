from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.router.media import get_user_id
from app.models.user import User as DBUser
from app.schema.user import UserCreate, UserResponse, UserLogin, UserUpdate, UserToken
import jwt

router = APIRouter()


def create_jwt(user_id, name, email):

    payload = {           
        "user_id": user_id,
        "name": name,
        "email": email
    }
    key = "your_secret"
    keyId = "your_key_id"

    jwt_assertion = jwt.encode(
        payload,
        key,
        algorithm='HS256',
        headers={
            'kid':keyId   #JWTへの署名に使用する公開キーのID
        }
    )
    return jwt_assertion

# ユーザー新規登録
@router.post("/signup", response_model=UserToken)
async def Signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = DBUser(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    token = create_jwt(db_user.id, db_user.name, db_user.email)
    return UserToken(token=token)


# ユーザーログイン
@router.post("/login", response_model=UserToken)
async def Login(user: UserLogin, db: Session = Depends(get_db)):
    # 入力を受け取る
    db_user = DBUser(**user.dict())
    # emailでレコード検索
    db_user = db.query(DBUser).filter(DBUser.email == user.email).first()
    # 対象のレコードのpasswordと入力されたpasswordがあっているか確認
    # あってたらtoken生成
    if db_user and user.hashed_password == db_user.hashed_password:
        token = create_jwt(db_user.id, db_user.name, db_user.email)
        return UserToken(token=token)
    else:
         raise HTTPException(status_code=401, detail="Incorrect email or password")

# ユーザー情報取得
@router.get("/user", response_model=UserResponse)
async def userinfo(
    user_id: int = Depends(get_user_id), 
    db: Session = Depends(get_db)
):
    user_info = db.query(DBUser).filter(DBUser.id == user_id).first()

    return user_info

    
# ユーザー情報アップデート
@router.patch("/user", response_model=UserResponse)
async def update_user(
    updated_user: UserUpdate,
    user_id: int = Depends(get_user_id),
    db: Session = Depends(get_db)
):
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.id != user_id:
        raise HTTPException(status_code=403, detail="User is not authorized to update this information")

    if updated_user.name:
        db_user.name = updated_user.name
    if updated_user.email:
        db_user.email = updated_user.email
    db.commit()
    db.refresh(db_user)

    return db_user

