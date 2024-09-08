from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserResponse
from repositories import user as user_repo
from db.base import get_db
from routers.auth import auth_user


router = APIRouter(prefix="/api/v1/users",
                   tags=["users"],
                   responses={404: {"message": "No encontrado"}})

@router.get("", response_model=list[UserResponse])
async def get_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), auth = Depends(auth_user)):
    users = user_repo.get_all_users(db, skip, limit)
    
    if len(users) == 0:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "No se han encontrado usuarios."
        )
    return users

@router.get("/{uuid}", response_model=UserResponse)
async def get_user_by_uuid(uuid: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    user = user_repo.get_user_by_uuid(db, uuid)
    
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            f"Usuario con uuid: '{uuid}' no encontrado"
        )
    
    return user