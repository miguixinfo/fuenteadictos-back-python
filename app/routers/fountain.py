from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from repositories import fountain as fountain_repo
from schemas.fountain import FountainCreate, FountainResponse
from db.base import get_db
from routers.auth import auth_user

router = APIRouter(prefix="/api/v1/fountains",
                   tags=["fountains"],
                   responses={404: {"message": "No encontrado"}})

@router.get("", response_model=list[FountainResponse])
async def get_all_fountains(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), auth = Depends(auth_user)): 
    fountains = fountain_repo.get_all_fountains(db, skip, limit)
    if len(fountains) == 0:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "No se han encontrado fuentes."
        )
    return fountains

@router.get("/{uuid}", response_model=FountainResponse)
async def get_fountain_by_uuid(uuid: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    fountain = fountain_repo.get_fountain_by_uuid(db, uuid)
    if not fountain:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            f"Fuente con uuid: '{uuid}' no encontrada"
        )
    return fountain

@router.get("/name/{name}", response_model=FountainResponse)
async def get_fountain_by_name(name: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    fountain = fountain_repo.get_fountain_by_name(db, name)
    if not fountain:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            f"Fuente con nombre: '{name}' no encontrada"
        )
    return fountain

@router.post("", response_model=FountainResponse)
async def create_fountain(fountain: FountainCreate, db: Session = Depends(get_db), auth = Depends(auth_user)):
    return fountain_repo.create_fountain(db, fountain) 