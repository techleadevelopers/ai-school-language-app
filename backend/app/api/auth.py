# app/api/auth.py
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.auth import LoginRequest, LoginResponse
from app.utils.token import create_access_token
from app.models.user import User

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest):
    user = User.get_by_email(payload.email)
    if not user or user.password != payload.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.id})
    return {"access_token": token, "token_type": "bearer"}
