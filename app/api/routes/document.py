from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.file_handler import normalize_and_save
from app.services.document_service import create_document_record
import uuid

router = APIRouter()


@router.post("/upload")
def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):

    document_id = str(uuid.uuid4())

    try:
        # Normalize & save file
        file_path = normalize_and_save(file, document_id)

        # Insert DB record
        new_doc = create_document_record(db, file_path)

        return {
            "document_id": new_doc.document_id,
            "status": new_doc.status,
            "file_path": new_doc.file_path
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
