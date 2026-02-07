from pydantic import BaseModel , Field 
from typing import List, Any , Optional


class LegalResponse(BaseModel):
    Summary: str = Field(description="Summary of the uploaded Document")
    Flag: str | None = Field(
        default=None,
        description="Risky clause  in the Document"
    ) 