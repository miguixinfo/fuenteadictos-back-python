from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from services import warning as warning_service
from schemas.warning import WarningCreate, WarningResponse
from db.base import get_db
from routers.auth import auth_user
from errors.errors import WarningNotFoundError, UserNotFoundError, FountainNotFoundError

router = APIRouter(prefix="/api/v1/warnings",
                   tags=["warnings"],
                   responses={404: {"message": "No encontrado"}})

@router.get("", response_model=list[WarningResponse])
async def get_all_warnings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return warning_service.get_all_warnings(db, skip, limit)
    except WarningNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.get("/{uuid}", response_model=WarningResponse)
async def get_warning_by_uuid(uuid: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return warning_service.get_warning_by_uuid(db, uuid)
    except WarningNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.get("/fountain/{uuid}", response_model=WarningResponse)
async def get_warnings_by_fountain_uuid(uuid: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return warning_service.get_warnings_by_fountain_uuid(db, uuid)
    except WarningNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.get("/user/{uuid}", response_model=WarningResponse)
async def get_warnings_by_user_uuid(uuid: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return warning_service.get_warnings_by_user_uuid(db, uuid)
    except WarningNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.post("", response_model=WarningResponse)
async def create_warning(warning: WarningCreate, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return warning_service.create_warning(db, warning)
    except UserNotFoundError as e:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            e.message
        )
    except FountainNotFoundError as e:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            e.message
        )