# app/schemas/lesson.py
from pydantic import BaseModel
from typing import Literal, Optional

class LessonBase(BaseModel):
    title: str
    level: str
    language: str
    type: Literal['reading', 'listening', 'speaking', 'question', 'chat']
    content: str

class LessonCreate(LessonBase):
    pass

class LessonResponse(LessonBase):
    id: int

    class Config:
        orm_mode = True
