from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.upload import router as upload_router
from database.database import engine
from database.models import Base
from routes.documents import router as documents_router

app = FastAPI(
    title="AI Document Reader",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(upload_router)
app.include_router(documents_router)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Backend is running 🚀"
    }