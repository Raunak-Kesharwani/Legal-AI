from fastapi import APIRouter

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from shared.schemas import SummaryResponse
import uuid

router = APIRouter()


@router.post("/summary", response_model=SummaryResponse)
async def summary(
    file: UploadFile | None = File(default=None),
    text: str | None = Form(default=None),
):
   
    if not file and not text:
        raise HTTPException(
            status_code=400,
            detail="Either file or text must be provided"
        )

    if file and text:
        raise HTTPException(
            status_code=400,
            detail="Provide only one of file or text"
        )

  
    document_id = f"doc_{uuid.uuid4().hex[:8]}"


    return SummaryResponse(
        document_id=document_id,
        summary="This is a dummy summary. Real summarization will be added later.",
        risk=None
    )
