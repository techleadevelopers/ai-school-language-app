
# app/schemas/progress.py
from pydantic import BaseModel

class ProgressBase(BaseModel):
    lesson_id: int
    user_id: int
    completed: bool = False
    score: float = 0.0

class ProgressCreate(ProgressBase):
    pass

class ProgressResponse(ProgressBase):
    id: int

    class Config:
        orm_mode = True
