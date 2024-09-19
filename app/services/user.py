from repositories import user as user_repo
from schemas.user import UserCreate
from errors.errors import UserNotFoundError

def get_all_users(db, skip: int = 0, limit: int = 0):
    users = user_repo.get_all_users(db, skip, limit)
    if len(users) == 0:
        raise UserNotFoundError(message="No se encontraron usuarios")
    return users


def get_user_by_uuid(db, uuid: str):
    user = user_repo.get_user_by_uuid(db, uuid)
    if not user:
        raise UserNotFoundError(param=uuid)
    return user

def retire_user(db, uuid: str):
    user = user_repo.retire_user(db, uuid)
    if not user:
        raise UserNotFoundError(param=uuid)
    return user