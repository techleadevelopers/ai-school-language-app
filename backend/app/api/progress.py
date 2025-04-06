
# app/api/progress.py
from fastapi import APIRouter
from app.models.progress import Progress

router = APIRouter()

@router.get("/user/progress")
def get_progress():
    return Progress.get_user_progress(1)
