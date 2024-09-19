from repositories import fountain as fountain_repo
from schemas.fountain import FountainCreate
from errors.errors import FountainNotFoundError, FountainAlreadyExistError

def get_all_fountains(db, skip: int = 0, limit: int = 0):
    fountains = fountain_repo.get_all_fountains(db, skip, limit)
    if len(fountains) == 0:
        raise FountainNotFoundError(message="No se encontraron fuentes")
    return fountains

def get_fountain_by_uuid(db, uuid: str):
    fountains = fountain_repo.get_fountain_by_uuid(db, uuid)
    if not fountains:
        raise FountainNotFoundError(param=uuid)
    return fountains

def get_fountains_by_name(db, name: str):
    fountains = fountain_repo.get_fountains_by_name(db, name)
    if len(fountains) == 0:
        raise FountainNotFoundError(message="No se han encontrado fuentes", param=name)
    return fountains

def create_fountain(db, fountain: FountainCreate):
    if fountain_repo.get_fountain_by_name(db, fountain.name):
        raise FountainAlreadyExistError()
    if (fountain_repo.get_fountain_by_location(db, fountain.latitude, fountain.longitude)):
        raise FountainAlreadyExistError()
    return fountain_repo.create_fountain(db, fountain)