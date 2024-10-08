from fastapi import FastAPI
from models import user, fountain, review, warning
from db.base import Base, engine
from routers import users, auth, fountain, warning, review

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Routers
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(fountain.router)
app.include_router(warning.router)
app.include_router(review.router)