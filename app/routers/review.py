from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from services import review as review_service
from schemas.review import ReviewCreate, ReviewResponse
from db.base import get_db
from routers.auth import auth_user
from errors.errors import ReviewNotFoundError, ReviewAlreadyExistError, UserNotFoundError, FountainNotFoundError

router = APIRouter(prefix="/api/v1/reviews",
                   tags=["reviews"],
                   responses={404: {"message": "No encontrado"}})

@router.get("", response_model=list[ReviewResponse])
async def get_all_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return review_service.get_all_reviews(db, skip, limit)
    except ReviewNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.get("/{uuid}", response_model=ReviewResponse)
async def get_review_by_uuid(uuid: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return review_service.get_review_by_uuid(db, uuid)
    except ReviewNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.get("/fountain/{uuid}", response_model=list[ReviewResponse])
async def get_reviews_by_fountain_uuid(uuid: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return review_service.get_reviews_by_fountain_uuid(db, uuid)
    except ReviewNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.get("/user/{uuid}", response_model=list[ReviewResponse])
async def get_reviews_by_user_uuid(uuid: str, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return review_service.get_reviews_by_user_uuid(db, uuid)
    except ReviewNotFoundError as e:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            e.message
        )

@router.post("", response_model=ReviewResponse)
async def create_review(review: ReviewCreate, db: Session = Depends(get_db), auth = Depends(auth_user)):
    try:
        return review_service.create_review(db, review)
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
    except ReviewAlreadyExistError as e:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            e.message
        )