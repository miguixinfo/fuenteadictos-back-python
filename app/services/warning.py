from repositories import warning as warning_repo
from schemas.warning import WarningCreate
from errors.errors import WarningNotFoundError, UserNotFoundError, FountainNotFoundError

def get_all_warnings(db, skip: int = 0, limit: int = 0):
    warnings = warning_repo.get_all_warnings(db, skip, limit)
    if len(warnings) == 0:
        raise WarningNotFoundError(message="No se encontraron advertencias")
    return warnings

def get_warning_by_uuid(db, uuid: str):
    warnings = warning_repo.get_warning_by_uuid(db, uuid)
    if not warnings:
        raise WarningNotFoundError(param=uuid)
    return warnings

def get_warnings_by_fountain_uuid(db, uuid: str):
    warnings = warning_repo.get_warnings_by_fountain_uuid(db, uuid)
    if len(warnings) == 0:
        raise WarningNotFoundError(param=uuid)
    return warnings

def get_warnings_by_user_uuid(db, uuid: str):
    warnings = warning_repo.get_warnings_by_user_uuid(db, uuid)
    if len(warnings) == 0:
        raise WarningNotFoundError(param=uuid)
    return warnings

def create_warning(db, warning: WarningCreate):
    user = warning_repo.get_user_by_uuid(db, warning.user_uuid)
    if not user:
        raise UserNotFoundError(param=warning.user_uuid)
    fountain = warning_repo.get_fountain_by_uuid(db, warning.fountain_uuid)
    if not fountain:
        raise FountainNotFoundError(param=warning.fountain_uuid)
    
    new_warning = Warning(warning.operative, user, fountain)
    return warning_repo.create_warning(db, new_warning)
        
def retire_warning(db, uuid: str):
    warning = warning_repo.retire_warning(db, uuid)
    if not warning:
        raise WarningNotFoundError(param=uuid)
    return warning