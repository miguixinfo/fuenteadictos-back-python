from passlib.context import CryptContext

# Configuración del contexto para bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para encriptar la contraseña
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Función para verificar la contraseña
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)