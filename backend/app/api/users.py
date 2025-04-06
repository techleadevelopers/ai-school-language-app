# app/api/users.py
from fastapi import APIRouter, Depends
from app.schemas.user import UserProfile

router = APIRouter()

@router.get("/user/profile", response_model=UserProfile)
def get_profile():
    return {
        "id": 1,
        "name": "Paulo",
        "email": "paulo@example.com",
        "role": "student",
        "avatar_url": "https://randomuser.me/api/portraits/men/1.jpg",
        "language_progress": {"english": 60.0, "spanish": 20.0}
    }
