from repositories import review as review_repo
from repositories import user as user_repo
from repositories import fountain as fountain_repo
from schemas.review import ReviewCreate
from models.review import Review
from errors.errors import ReviewNotFoundError, ReviewAlreadyExistError, UserNotFoundError, FountainNotFoundError

def get_all_reviews(db, skip: int = 0, limit: int = 0):
    reviews = review_repo.get_all_reviews(db, skip, limit)
    if len(reviews) == 0:
        raise ReviewNotFoundError(message="No se encontraron reseñas")
    return reviews

def get_review_by_uuid(db, uuid: str):
    reviews = review_repo.get_review_by_uuid(db, uuid)
    if not reviews:
        raise ReviewNotFoundError(param=uuid)
    return reviews

def get_reviews_by_fountain_uuid(db, uuid: str):
    reviews = review_repo.get_reviews_by_fountain_uuid(db, uuid)
    if len(reviews) == 0:
        raise ReviewNotFoundError(param=uuid)
    return reviews

def get_reviews_by_user_uuid(db, uuid: str):
    reviews = review_repo.get_reviews_by_user_uuid(db, uuid)
    if len(reviews) == 0:
        raise ReviewNotFoundError(param=uuid)
    return reviews

def create_review(db, review: ReviewCreate):
    user = user_repo.get_user_by_uuid(db, review.user_uuid)
    if not user:
        raise UserNotFoundError(param=review.user_uuid)
    fountain = fountain_repo.get_fountain_by_uuid(db, review.fountain_uuid)
    if not fountain:
        raise FountainNotFoundError(param=review.fountain_uuid)

    validate_review(db, user.id, fountain.id) 
    new_review = Review(header=review.header, description=review.description,
                        jet_points=review.jet_points, cold_points=review.cold_points,
                        pretty_points=review.pretty_points, flavor_points=review.flavor_points,
                        user_id=user.id, fountain_id=fountain.id)
    return review_repo.create_review(db, new_review)

def validate_review(db, user_uuid: str, fountain_uuid: str):
    if review_repo.validate_review(db, user_uuid, fountain_uuid):
        raise ReviewAlreadyExistError(message="Ya existe una review de esta fuente para este usuario")