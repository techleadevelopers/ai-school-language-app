
# app/schemas/response.py
from pydantic import BaseModel
from typing import Optional

class WhisperFeedback(BaseModel):
    transcript: str
    feedback: Optional[str]
    score: Optional[float]

class LeaderboardEntry(BaseModel):
    user_id: int
    name: str
    avatar_url: Optional[str]
    score: int

class GenericResponse(BaseModel):
    success: bool
    message: Optional[str] = None