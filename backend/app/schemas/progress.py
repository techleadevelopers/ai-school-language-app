
# app/schemas/progress.py
from pydantic import BaseModel
from typing import Optional, Dict, List, Any
from datetime import datetime

class ProgressBase(BaseModel):
    lesson_id: int
    user_id: int
    percent_complete: float = 0.0
    is_completed: bool = False

class ProgressCreate(ProgressBase):
    pass

class ProgressUpdate(BaseModel):
    percent_complete: Optional[float] = None
    accuracy_score: Optional[float] = None
    fluency_score: Optional[float] = None
    pronunciation_score: Optional[float] = None
    time_spent_minutes: Optional[int] = None
    xp_gained: Optional[int] = None
    course_data: Optional[Dict[str, Any]] = None
    learning_objectives: Optional[List[str]] = None
    strengths: Optional[List[str]] = None
    weaknesses: Optional[List[str]] = None

class SessionData(BaseModel):
    duration_minutes: int
    accuracy: float
    fluency: float
    pronunciation: float
    xp_earned: int
    lesson_completed: bool = False

class CourseData(BaseModel):
    course_id: str
    course_name: str
    language: str
    difficulty_level: str
    modules_completed: List[str] = []
    current_module: str
    estimated_completion_time: int
    custom_settings: Dict[str, Any] = {}

class ProgressResponse(BaseModel):
    id: int
    user_id: int
    lesson_id: int
    percent_complete: float
    is_completed: bool
    current_level: str
    xp_gained: int
    total_xp: int
    streak_count: int
    accuracy_score: float
    fluency_score: float
    pronunciation_score: float
    time_spent_minutes: int
    session_count: int
    course_data: Dict[str, Any]
    learning_objectives: List[str]
    strengths: List[str]
    weaknesses: List[str]
    started_at: datetime
    last_updated: datetime
    completed_at: Optional[datetime]

    class Config:
        orm_mode = True
