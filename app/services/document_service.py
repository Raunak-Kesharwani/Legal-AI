import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from app.db.models import Document


def create_document_record(db: Session, file_path: str):
    document_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()

    new_doc = Document(
        document_id=document_id,
        file_path=file_path,
        created_at=now,
        updated_at=now,
        status="uploaded",
        final_summary=None,
        risk_flag=None,
        chunk_summaries=None,
        num_chunks=None,
    )

    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    return new_doc
