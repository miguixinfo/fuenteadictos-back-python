from sqlalchemy.orm import Session
from models.warning import Warning
from models.fountain import Fountain
from models.user import User

def get_warning_by_uuid(db: Session, uuid: str) -> Warning:
    return db.query(Warning).filter(Warning.uuid == uuid).first()

def get_all_warnings(db: Session, skip: int = 0, limit: int = 0) -> list:
    return db.query(Warning).offset(skip).limit(limit).all()

def get_warnings_by_fountain_uuid(db: Session, uuid: str) -> Warning:
    return db.query(Warning).join(Fountain, Fountain.id == Warning.fountain_id).filter(
        Fountain.uuid == uuid).all()

def get_warnings_by_user_uuid(db: Session, uuid: str) -> Warning:
    return db.query(Warning).join(User, User.id == Warning.user_id).filter(
        User.uuid == uuid).all()

def create_warning(db: Session, warning: Warning) -> Warning:
    db_warning = Warning(operative=warning.operative, user_id=warning.user_id,
                         fountain_id=warning.fountain_id)  
    
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
