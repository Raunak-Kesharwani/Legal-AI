from fastapi import APIRouter, UploadFile, File
from backend.core.summarizer import LegalSummarizer

router = APIRouter()

@router.post("/summary")
def summary():
    pass
