from fastapi import FastAPI
from app.db.database import engine
from app.db import models
from app.api.routes import document, chat

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Legal AI Backend")

app.include_router(document.router, prefix="/documents", tags=["Documents"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

