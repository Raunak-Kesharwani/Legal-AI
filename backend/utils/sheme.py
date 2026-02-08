from pydantic import BaseModel, Field
from typing import Optional

class ChunkLegalResponse(BaseModel):
    Summary: str = Field(
        description="Detailed summary of this section"
    )
    Flag: Optional[str] = Field(
        default=None,
        description="Risky clause if present"
    )


class FinalLegalResponse(BaseModel):
    Summary: str = Field(
        min_length=600,
        description="Full multi-paragraph legal summary"
    )
    Flag: Optional[str] = Field(
        description="Most significant risky clause for bearer"
    )
