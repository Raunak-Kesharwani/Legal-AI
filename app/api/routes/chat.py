from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def dummy_chat():
    return {"message": "Chat endpoint working (dummy)"}
