from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(email=user.email, username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_uuid(db: Session, user_uuid: str) -> User:
    return db.query(User).filter(User.uuid == user_uuid).first()

def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 0) -> list:
    return db.query(User).offset(skip).limit(limit).all()

def delete_user(db: Session, uuid: str):
    user = get_user_by_uuid(uuid)
    if user:
        db.delete(user)
        db.commit()
    return user
    