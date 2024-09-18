from sqlalchemy.orm import Session
from models.fountain import Fountain
from schemas.user import FountainCreate

def get_fountain_by_uuid(db: Session, uuid: str) -> Fountain:
    return db.query(Fountain).filter(Fountain.uuid == uuid).first()

def get_all_fountains(db: Session, skip: int = 0, limit: int = 0) -> list:
    return db.query(Fountain).offset(skip).limit(limit).all()

def get_fountain_by_name(db: Session, name: str) -> Fountain:
    return db.query(Fountain).filter(Fountain.name.ilike(f"%{name}%")).first()

def create_fountain(db: Session, fountain: FountainCreate) -> Fountain:
    db_fountain = Fountain(name=fountain.name, description=fountain.description, image=fountain.image,
                           operative=fountain.operative, latitude=fountain.latitude, longitude=fountain.longitude)
    db.add(db_fountain)
    db.commit()
    db.refresh(db_fountain)
    return db_fountain