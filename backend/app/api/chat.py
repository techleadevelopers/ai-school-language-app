# app/api/chat.py
from fastapi import APIRouter
from app.schemas.lesson import ChatRequest
from app.services.mistral_service import chat_with_mistral

router = APIRouter()

@router.post("/chat")
def chat_with_ia(payload: ChatRequest):
    response = chat_with_mistral(payload.messages, payload.context)
    return {"response": response}
