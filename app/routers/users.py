from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserResponse
from services import user as user_service 
from db.base import get_db
from routers.auth import auth_user
from errors.errors import UserNotFoundError


router = APIRouter(prefix="/api/v1/users",
                   tags=["users"],
                   responses={404: {"message": "No encontrado"}})

@router.get("", response_model=list[UserResponse])
async def get_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return user_service.get_all_users(db, skip, limit)
    except UserNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.get("/{uuid}", response_model=UserResponse)
async def get_user_by_uuid(uuid: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return user_service.get_user_by_uuid(db, uuid)
    except UserNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.delete("/{uuid}", response_model=UserResponse)
async def retire_user(uuid: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return user_service.retire_user(db, uuid)
    except UserNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )