from fastapi import APIRouter
from app.models import ChatRequest, ChatResponse
from app.chat import get_chat_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    # Placeholder logic
    return get_chat_response(request) 