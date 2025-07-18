
# app/api/progress.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.progress import Progress
from app.models.user import User
from app.schemas.progress import (
    ProgressCreate, 
    ProgressUpdate, 
    ProgressResponse, 
    SessionData,
    CourseData
)
from app.utils.token import get_current_user
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/user/progress", response_model=List[ProgressResponse])
async def get_user_progress(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obter todo o progresso do usuário"""
    try:
        user_progress = db.query(Progress).filter(
            Progress.user_id == current_user["user_id"]
        ).all()
        
        return user_progress
    except Exception as e:
        logger.error(f"Error fetching user progress: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch progress")

@router.get("/user/progress/{lesson_id}", response_model=ProgressResponse)
async def get_lesson_progress(
    lesson_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obter progresso de uma lição específica"""
    try:
        progress = db.query(Progress).filter(
            Progress.user_id == current_user["user_id"],
            Progress.lesson_id == lesson_id
        ).first()
        
        if not progress:
            raise HTTPException(status_code=404, detail="Progress not found")
        
        return progress
    except Exception as e:
        logger.error(f"Error fetching lesson progress: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch lesson progress")

@router.post("/user/progress", response_model=ProgressResponse)
async def create_progress(
    progress_data: ProgressCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Criar novo progresso para uma lição"""
    try:
        # Verificar se já existe progresso para essa lição
        existing_progress = db.query(Progress).filter(
            Progress.user_id == current_user["user_id"],
            Progress.lesson_id == progress_data.lesson_id
        ).first()
        
        if existing_progress:
            raise HTTPException(status_code=400, detail="Progress already exists for this lesson")
        
        # Criar novo progresso
        new_progress = Progress(
            user_id=current_user["user_id"],
            lesson_id=progress_data.lesson_id,
            percent_complete=progress_data.percent_complete,
            is_completed=progress_data.is_completed
        )
        
        db.add(new_progress)
        db.commit()
        db.refresh(new_progress)
        
        logger.info(f"Created progress for user {current_user['user_id']}, lesson {progress_data.lesson_id}")
        return new_progress
        
    except Exception as e:
        logger.error(f"Error creating progress: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create progress")

@router.put("/user/progress/{lesson_id}", response_model=ProgressResponse)
async def update_progress(
    lesson_id: int,
    progress_data: ProgressUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Atualizar progresso de uma lição"""
    try:
        progress = db.query(Progress).filter(
            Progress.user_id == current_user["user_id"],
            Progress.lesson_id == lesson_id
        ).first()
        
        if not progress:
            raise HTTPException(status_code=404, detail="Progress not found")
        
        # Atualizar campos fornecidos
        update_data = progress_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(progress, field, value)
        
        db.commit()
        db.refresh(progress)
        
        logger.info(f"Updated progress for user {current_user['user_id']}, lesson {lesson_id}")
        return progress
        
    except Exception as e:
        logger.error(f"Error updating progress: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update progress")

@router.post("/user/progress/{lesson_id}/session")
async def save_session_data(
    lesson_id: int,
    session_data: SessionData,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Salvar dados de uma sessão de estudo"""
    try:
        progress = db.query(Progress).filter(
            Progress.user_id == current_user["user_id"],
            Progress.lesson_id == lesson_id
        ).first()
        
        if not progress:
            # Criar progresso se não existir
            progress = Progress(
                user_id=current_user["user_id"],
                lesson_id=lesson_id
            )
            db.add(progress)
        
        # Atualizar progresso com dados da sessão
        progress.update_progress(session_data.dict())
        
        db.commit()
        db.refresh(progress)
        
        logger.info(f"Saved session data for user {current_user['user_id']}, lesson {lesson_id}")
        return {"success": True, "message": "Session data saved successfully"}
        
    except Exception as e:
        logger.error(f"Error saving session data: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to save session data")

@router.post("/user/progress/{lesson_id}/course-data")
async def save_course_data(
    lesson_id: int,
    course_data: CourseData,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Salvar dados específicos do curso"""
    try:
        progress = db.query(Progress).filter(
            Progress.user_id == current_user["user_id"],
            Progress.lesson_id == lesson_id
        ).first()
        
        if not progress:
            # Criar progresso se não existir
            progress = Progress(
                user_id=current_user["user_id"],
                lesson_id=lesson_id
            )
            db.add(progress)
        
        # Salvar dados do curso
        progress.save_course_data(course_data.dict())
        
        db.commit()
        db.refresh(progress)
        
        logger.info(f"Saved course data for user {current_user['user_id']}, lesson {lesson_id}")
        return {"success": True, "message": "Course data saved successfully"}
        
    except Exception as e:
        logger.error(f"Error saving course data: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to save course data")

@router.get("/user/progress/statistics")
async def get_progress_statistics(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obter estatísticas de progresso do usuário"""
    try:
        user_progress = db.query(Progress).filter(
            Progress.user_id == current_user["user_id"]
        ).all()
        
        if not user_progress:
            return {"message": "No progress data found"}
        
        # Calcular estatísticas
        total_lessons = len(user_progress)
        completed_lessons = sum(1 for p in user_progress if p.is_completed)
        total_xp = sum(p.total_xp for p in user_progress)
        total_time = sum(p.time_spent_minutes for p in user_progress)
        avg_accuracy = sum(p.accuracy_score for p in user_progress) / total_lessons if total_lessons > 0 else 0
        
        return {
            "total_lessons": total_lessons,
            "completed_lessons": completed_lessons,
            "completion_rate": (completed_lessons / total_lessons) * 100 if total_lessons > 0 else 0,
            "total_xp": total_xp,
            "total_time_minutes": total_time,
            "total_time_hours": total_time / 60,
            "average_accuracy": avg_accuracy,
            "current_streak": max(p.streak_count for p in user_progress) if user_progress else 0
        }
        
    except Exception as e:
        logger.error(f"Error calculating progress statistics: {e}")
        raise HTTPException(status_code=500, detail="Failed to calculate statistics")
