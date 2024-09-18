from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from core.config import settings
from repositories import user as user_repo
from schemas.user import UserResponse, UserCreate
from sqlalchemy.orm import Session
from db.base import get_db
from utils import encrypt
 
router = APIRouter(prefix="/api/v1/auth",
                   tags=["auth"],
                   responses={404: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

async def auth_user(token: str = Depends(oauth2), db: Session = Depends(get_db)):
    exception = HTTPException(status.HTTP_401_UNAUTHORIZED,
                              "Credenciales de autenticación inválidas",
                              headers={"WWW-Authenticate": "Bearer"})
    
    try:
        username = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]).get("sub")
        if not username:
            raise exception
    except JWTError:
        raise exception
    
    return user_repo.get_user_by_username(db, username)
    
# async def current_user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_db = user_repo.get_user_by_username(db, form.username)
    if not user_db:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, "El usuario no es correcto"
        )
        
    if not encrypt.verify_password(form.password, user_db.password):
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, "La contraseña no es correcta"
        ) 
        
    access_token = {
        "sub": user_db.username,
        "exp": datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    
    return {"access_token": jwt.encode(access_token, settings.SECRET_KEY, settings.ALGORITHM), "token_type": "bearer"}



@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_repo.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = encrypt.hash_password(user.password)
    new_user = UserCreate(
                                     email=user.email,
                                     username=user.username,
                                     password=hashed_password,
                                 )
    return user_repo.create_user(db, new_user)

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: UserResponse = Depends(auth_user)):
    return current_user