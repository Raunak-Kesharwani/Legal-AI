from fastapi import APIRouter, HTTPException
from shared.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Dummy chat endpoint.
    Validates request and returns a placeholder answer.
    """

    # 1️⃣ Basic validation (MVP)
    if not request.document_id.strip():
        raise HTTPException(
            status_code=400,
            detail="Invalid document_id"
        )

    # 2️⃣ Dummy response
    return ChatResponse(
        answer=f"This is a dummy response for your question: '{request.query}'"
    )
