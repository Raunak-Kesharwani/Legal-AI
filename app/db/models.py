from sqlalchemy import Column, String, Text, Integer
from app.db.database import Base


class Document(Base):
    __tablename__ = "documents"

    document_id = Column(String, primary_key=True, index=True)
    file_path = Column(String, nullable=False)

    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)
    status = Column(String, nullable=False)

    final_summary = Column(Text, nullable=True)
    risk_flag = Column(Text, nullable=True)

    chunk_summaries = Column(Text, nullable=True)  # stored as JSON string
    num_chunks = Column(Integer, nullable=True)
