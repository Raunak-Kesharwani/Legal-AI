from fastapi import FastAPI
from backend.api.summary import router as summary_router 
from backend.api.health import router as health_router
from backend.api.chat import router as chat_router

app = FastAPI(title="Legal-AI")

app.include_router(summary_router, prefix="/api")
app.include_router(health_router, prefix="/api")
app.include_router(chat_router, prefix="/api")