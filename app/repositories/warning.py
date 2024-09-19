from sqlalchemy.orm import Session
from models.warning import Warning
from models.warning import Warning

def get_warning_by_uuid(db: Session, uuid: str) -> Warning:
    return db.query(Warning).filter(Warning.uuid == uuid).first()

def get_all_warnings(db: Session, skip: int = 0, limit: int = 0) -> list:
    return db.query(Warning).offset(skip).limit(limit).all()

def get_warnings_by_fountain_uuid(db: Session, uuid: str) -> Warning:
    return db.query(Warning).filter(Warning.fountain_uuid == uuid).all()

def get_warnings_by_user_uuid(db: Session, uuid: str) -> Warning:
    return db.query(Warning).filter(Warning.user_uuid == uuid).all()

def create_warning(db: Session, warning: Warning) -> Warning:
    db_warning = Warning(**warning.model_dump())
    db.add(db_warning)
    db.commit()
    db.refresh(db_warning)
    return db_warning

def retire_warning(db: Session, uuid: str):
    warning = get_warning_by_uuid(db, uuid)
    if warning:
        db.delete(warning)
        db.commit()
    return warning
