
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from typing import Dict, Any
import asyncio
from datetime import datetime, timedelta

from ..services.pdf_report_service import pdf_report_service
from ..utils.token import verify_token

router = APIRouter()

@router.get("/weekly-report/{user_id}")
async def generate_weekly_report(
    user_id: str,
    token_data: dict = Depends(verify_token)
):
    """
    Generate comprehensive weekly progress report
    """
    try:
        # Mock user data - replace with actual database queries
        user_data = await get_user_report_data(user_id)
        
        # Generate PDF report
        pdf_bytes = await pdf_report_service.generate_weekly_report(user_id, user_data)
        
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f"attachment; filename=bilingui_weekly_report_{user_id}_{datetime.now().strftime('%Y%m%d')}.pdf"
            }
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate report: {str(e)}")

@router.get("/monthly-report/{user_id}")
async def generate_monthly_report(
    user_id: str,
    token_data: dict = Depends(verify_token)
):
    """
    Generate comprehensive monthly progress report
    """
    try:
        # Mock user data for monthly report
        user_data = await get_user_monthly_data(user_id)
        
        # Generate PDF report (similar to weekly but with monthly data)
        pdf_bytes = await pdf_report_service.generate_weekly_report(user_id, user_data)
        
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f"attachment; filename=bilingui_monthly_report_{user_id}_{datetime.now().strftime('%Y%m')}.pdf"
            }
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate monthly report: {str(e)}")

async def get_user_report_data(user_id: str) -> Dict[str, Any]:
    """
    Get comprehensive user data for report generation
    """
    # This would typically fetch from database
    # For now, returning mock data
    return {
        "name": "João Silva",
        "email": "joao@example.com",
        "level": 15,
        "total_xp": 7500,
        "streak": 12,
        "start_date": "2024-01-15",
        
        # Weekly metrics
        "lessons_completed": 8,
        "prev_lessons_completed": 6,
        "study_time": 240,
        "prev_study_time": 180,
        "avg_score": 87.5,
        "prev_avg_score": 82.3,
        "xp_gained": 450,
        "prev_xp_gained": 320,
        
        # Learning breakdown
        "pronunciation_time": 60,
        "pronunciation_accuracy": 78.5,
        "pronunciation_progress": 68.0,
        "vocabulary_time": 90,
        "vocabulary_accuracy": 92.1,
        "vocabulary_progress": 85.5,
        "grammar_time": 70,
        "grammar_accuracy": 85.7,
        "grammar_progress": 72.8,
        "conversation_time": 20,
        "conversation_accuracy": 76.3,
        "conversation_progress": 45.2,
        
        # Daily XP for chart
        "daily_xp": [50, 75, 120, 90, 110, 80, 140],
        
        # AI insights
        "strengths": ["Vocabulário", "Compreensão auditiva", "Leitura"],
        "weaknesses": ["Pronúncia", "Conversação fluente", "Gramática avançada"],
        "ai_insights": [
            "Você demonstra excelente progresso em vocabulário básico.",
            "Recomenda-se mais prática em pronúncia de sons específicos como 'th' e 'r'.",
            "Seu padrão de estudo é consistente - continue assim!",
            "Considere aumentar a prática de conversação para melhorar a fluência."
        ],
        
        # Goals and recommendations
        "weekly_goals": [
            "Completar 5 lições de pronúncia",
            "Manter sequência de estudos por 7 dias",
            "Alcançar 85% de precisão em exercícios",
            "Praticar conversação por 30 minutos"
        ],
        "recommendations": [
            "Foque em exercícios de listening com sotaque americano",
            "Use a ferramenta de chat com IA para praticar conversação",
            "Revise verbos irregulares 2-3 vezes por semana",
            "Participe dos desafios multiplayer para maior motivação"
        ]
    }

async def get_user_monthly_data(user_id: str) -> Dict[str, Any]:
    """
    Get monthly user data for report generation
    """
    # Similar to weekly but with extended timeframe
    weekly_data = await get_user_report_data(user_id)
    
    # Modify for monthly context
    weekly_data.update({
        "lessons_completed": 32,
        "prev_lessons_completed": 28,
        "study_time": 960,
        "prev_study_time": 840,
        "xp_gained": 1800,
        "prev_xp_gained": 1520,
        "daily_xp": [50, 75, 120, 90, 110, 80, 140] * 4  # 4 weeks
    })
    
    return weekly_data
