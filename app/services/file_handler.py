import os
import uuid
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader

UPLOAD_DIR = "uploads"

# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)


def normalize_and_save(file, document_id: str) -> str:
    """
    Convert uploaded file to normalized .txt
    and store it as uploads/{document_id}.txt
    """

    file_ext = file.filename.split(".")[-1].lower()
    temp_path = f"{UPLOAD_DIR}/{document_id}_temp.{file_ext}"

    # Save uploaded file temporarily
    with open(temp_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Extract text
    if file_ext == "pdf":
        loader = PyPDFLoader(temp_path)
        docs = loader.load()
        text = "\n".join(doc.page_content for doc in docs)

    elif file_ext == "txt":
        loader = TextLoader(temp_path, encoding="utf-8")
        docs = loader.load()
        text = "\n".join(doc.page_content for doc in docs)

    else:
        os.remove(temp_path)
        raise ValueError("Unsupported file type")

    # Save normalized txt
    final_path = f"{UPLOAD_DIR}/{document_id}.txt"
    with open(final_path, "w", encoding="utf-8") as f:
        f.write(text)

    # Remove temp file
    os.remove(temp_path)

    return final_path
