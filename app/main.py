from fastapi import FastAPI
from models import user, fountain, review, warning
from db.base import Base, engine
from routers import users, auth, fountain, warning, review
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowed origins
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# Routers
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(fountain.router)
app.include_router(warning.router)
app.include_router(review.router)