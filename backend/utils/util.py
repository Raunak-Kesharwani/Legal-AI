from typing import List

def cap_chunks(chunks: List[str], max_chunks: int = 9) -> List[str]:
    """
    Limit the number of chunks to at most max_chunks
    by evenly sampling across the document.
    """
    if len(chunks) <= max_chunks:
        return chunks

    step = max(1, len(chunks) // max_chunks)
    return [chunks[i] for i in range(0, len(chunks), step)][:max_chunks]


def truncate_text(text: str, max_chars: int = 8000) -> str:
    """
    Prevent silent LLM failures by bounding input size.
    """
    if len(text) <= max_chars:
        return text
    return text[:max_chars]
