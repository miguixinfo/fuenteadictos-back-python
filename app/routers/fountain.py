from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from services import fountain as fountain_service
from schemas.fountain import FountainCreate, FountainResponse
from db.base import get_db
from routers.auth import auth_user
from errors.errors import FountainAlreadyExistError, FountainNotFoundError

router = APIRouter(prefix="/api/v1/fountains",
                   tags=["fountains"],
                   responses={404: {"message": "No encontrado"}})

@router.get("", response_model=list[FountainResponse])
async def get_all_fountains(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), auth = Depends(auth_user)): 
    try:
        return fountain_service.get_all_fountains(db, skip, limit)
    except FountainNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )
        
@router.get("/{uuid}", response_model=FountainResponse)
async def get_fountain_by_uuid(uuid: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return fountain_service.get_fountain_by_uuid(db, uuid)
    except FountainNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.get("/name/{name}", response_model=list[FountainResponse])
async def get_fountain_by_name(name: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return fountain_service.get_fountains_by_name(db, name)
    except FountainNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.post("", response_model=FountainResponse)
async def create_fountain(fountain: FountainCreate, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return fountain_service.create_fountain(db, fountain) 
    except FountainAlreadyExistError as e:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            e.message
        )