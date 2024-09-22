from sqlalchemy.orm import Session
from models.review import Review
from models.user import User
from models.fountain import Fountain

def get_all_reviews(db: Session, skip: int = 0, limit: int = 0) -> list:
    return db.query(Review).offset(skip).limit(limit).all()

def get_review_by_uuid(db: Session, uuid: str) -> Review:
    return db.query(Review).filter(Review.uuid == uuid).first()

def get_reviews_by_fountain_uuid(db: Session, uuid: str) -> Review:
    return db.query(Review).join(Fountain, Fountain.id == Review.fountain_id).filter(
        Fountain.uuid == uuid).all()

def get_reviews_by_user_uuid(db: Session, uuid: str) -> Review:
    return db.query(Review).join(User, User.id == Review.user_id).filter(
        User.uuid == uuid).all()

def create_review(db: Session, review: Review) -> Review:
    db_review = Review(header=review.header, description=review.description,
                       jet_points=review.jet_points, cold_points=review.cold_points,
                       pretty_points=review.pretty_points, flavor_points=review.flavor_points,
                       user_id=review.user_id, fountain_id=review.fountain_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def retire_review(db: Session, uuid: str):
    review = get_review_by_uuid(db, uuid)
    if review:
        db.delete(review)
        db.commit()
    return review

def validate_review(db: Session, user_id: str, fountain_id: str):
    return db.query(Review).filter(Review.user_id == user_id).filter(Review.fountain_id == fountain_id).first()