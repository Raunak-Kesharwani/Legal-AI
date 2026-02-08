from pydantic import BaseModel, Field
from typing import Optional


class TextSummaryRequest(BaseModel):
    text: str = Field(
        min_length=50,
        description="Full document content pasted by the user"
    )

class SummaryResponse(BaseModel):
    document_id: str = Field(
        description="Unique identifier for the uploaded document"
    )
    summary: str = Field(
        description="Multi-paragraph document summary"
    )
    risk: Optional[str] = Field(
        default=None,
        description="Risky or harmful clause if any"
    )


class ChatRequest(BaseModel):
    document_id: str = Field(
        description="Document ID returned from summary endpoint"
    )
    query: str = Field(
        min_length=5,
        description="User question about the document"
    )


class ChatResponse(BaseModel):
    answer: str = Field(
        description="Answer generated using the document content"
    )

class ErrorResponse(BaseModel):
    detail: str
