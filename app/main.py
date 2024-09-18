from fastapi import FastAPI
from models import user, fountain, review, warning
from db.base import Base, engine
from routers import users, auth, fountain

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Routers
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(fountain.router)