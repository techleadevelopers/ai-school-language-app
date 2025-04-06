
# app/schemas/chat_log.py
from pydantic import BaseModel
from typing import Optional

class ChatLogBase(BaseModel):
    user_id: int
    message: str
    response: Optional[str] = None
    lesson_id: Optional[int]

class ChatLogCreate(ChatLogBase):
    pass

class ChatLogResponse(ChatLogBase):
    id: int

    class Config:
        orm_mode = True
