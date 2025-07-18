
from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, List, Optional
import logging
from datetime import datetime, timedelta

from app.services.advanced_learning_engine import advanced_learning_engine
from app.services.speech_analysis_engine import speech_analysis_engine
from app.services.gamification_engine import gamification_engine

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/learning-profile/{user_id}")
async def get_learning_profile(user_id: str):
    """
    Obter perfil de aprendizado completo do usuário
    """
    try:
        # Buscar histórico de performance (em produção, do banco de dados)
        performance_history = []  # Simular busca do BD
        
        # Analisar padrões de aprendizado
        learning_profile = await advanced_learning_engine.analyze_learning_pattern(
            user_id, performance_history
        )
        
        return {
            "success": True,
            "data": learning_profile,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Learning profile retrieval failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/adaptive-content/{user_id}")
async def generate_adaptive_content(user_id: str, lesson_type: str = "general"):
    """
    Gerar conteúdo adaptativo personalizado
    """
    try:
        adaptive_content = await advanced_learning_engine.generate_adaptive_content(
            user_id, lesson_type
        )
        
        return {
            "success": True,
            "data": adaptive_content,
            "personalization_level": "high",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Adaptive content generation failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/learning-optimization/{user_id}")
async def optimize_learning_path(user_id: str):
    """
    Otimizar caminho de aprendizado do usuário
    """
    try:
        optimization_plan = await advanced_learning_engine.optimize_learning_path(user_id)
        
        return {
            "success": True,
            "data": optimization_plan,
            "optimization_confidence": 0.92,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Learning optimization failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/real-time-coaching/{user_id}")
async def provide_real_time_coaching(user_id: str, performance_data: Dict):
    """
    Fornecer coaching em tempo real
    """
    try:
        coaching_response = await advanced_learning_engine.provide_real_time_coaching(
            user_id, performance_data
        )
        
        return {
            "success": True,
            "data": coaching_response,
            "coaching_type": "real_time",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Real-time coaching failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/advanced-speech-analysis/{user_id}")
async def analyze_speech_advanced(user_id: str, 
                                audio_data: Dict,
                                target_text: str,
                                native_language: str = "pt"):
    """
    Análise avançada de fala com feedback detalhado
    """
    try:
        # Em produção, processar áudio real
        audio_bytes = b""  # Simular dados de áudio
        
        analysis_result = await speech_analysis_engine.analyze_pronunciation_advanced(
            audio_bytes, target_text, user_id, native_language
        )
        
        return {
            "success": True,
            "data": analysis_result,
            "analysis_type": "advanced_pronunciation",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Advanced speech analysis failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/gamification/profile/{user_id}")
async def get_gamification_profile(user_id: str):
    """
    Obter perfil completo de gamificação
    """
    try:
        # Simular dados do usuário
        user_stats = {
            "total_xp": 5000,
            "current_level": 12,
            "streak_days": 15,
            "lessons_completed": 45,
            "achievements_unlocked": 8
        }
        
        # Verificar achievements
        new_achievements = await gamification_engine.check_achievements(user_id, user_stats)
        
        # Atualizar streak
        streak_data = await gamification_engine.update_streak(user_id)
        
        # Criar desafios personalizados
        personalized_challenges = await gamification_engine.create_personalized_challenges(
            user_id, user_stats
        )
        
        # Gerar conteúdo motivacional
        motivation_content = await gamification_engine.generate_motivation_content(
            user_id, user_stats
        )
        
        gamification_profile = {
            "user_stats": user_stats,
            "new_achievements": new_achievements,
            "streak_data": streak_data,
            "personalized_challenges": personalized_challenges,
            "motivation_content": motivation_content,
            "level_progress": {
                "current_level": user_stats["current_level"],
                "current_xp": user_stats["total_xp"],
                "xp_for_next_level": (user_stats["current_level"] + 1) * 500,
                "progress_percentage": 75
            }
        }
        
        return {
            "success": True,
            "data": gamification_profile,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Gamification profile retrieval failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/leaderboard/{leaderboard_type}")
async def get_leaderboard(leaderboard_type: str = "weekly", user_id: Optional[str] = None):
    """
    Obter leaderboard dinâmico
    """
    try:
        leaderboard_data = await gamification_engine.generate_leaderboard(
            leaderboard_type, user_id
        )
        
        return {
            "success": True,
            "data": leaderboard_data,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Leaderboard retrieval failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/calculate-xp/{user_id}")
async def calculate_xp_reward(user_id: str, activity_data: Dict):
    """
    Calcular recompensa XP para atividade
    """
    try:
        activity_type = activity_data.get("type", "general")
        performance_data = activity_data.get("performance", {})
        
        xp_calculation = await gamification_engine.calculate_xp_reward(
            activity_type, performance_data, user_id
        )
        
        return {
            "success": True,
            "data": xp_calculation,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"XP calculation failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/insights/comprehensive/{user_id}")
async def get_comprehensive_insights(user_id: str):
    """
    Obter insights abrangentes de aprendizado
    """
    try:
        logger.info(f"📊 Generating comprehensive insights for user: {user_id}")
        
        # Combinar dados de múltiplos engines
        learning_insights = await advanced_learning_engine.analyze_learning_pattern(user_id, [])
        
        # Análise de progresso de fala
        speech_progress = {
            "pronunciation_trend": "improving",
            "fluency_development": "steady",
            "areas_of_focus": ["th_sounds", "rhythm"],
            "mastered_skills": ["basic_vowels", "common_words"]
        }
        
        # Dados de gamificação
        gamification_insights = {
            "motivation_level": "high",
            "engagement_score": 0.85,
            "consistency_rating": "excellent",
            "social_interaction": "active"
        }
        
        # Predições de sucesso
        success_predictions = {
            "fluency_timeline": "6-8 months",
            "next_milestone": "Intermediate proficiency",
            "success_probability": 0.88,
            "recommended_focus": ["conversation_practice", "pronunciation_refinement"]
        }
        
        comprehensive_insights = {
            "learning_analytics": learning_insights,
            "speech_progress": speech_progress,
            "gamification_insights": gamification_insights,
            "success_predictions": success_predictions,
            "actionable_recommendations": [
                "Increase conversation practice frequency",
                "Focus on pronunciation consistency",
                "Engage more with community features",
                "Set daily learning goals"
            ],
            "progress_summary": {
                "overall_progress": "85%",
                "strengths": ["Consistency", "Pronunciation"],
                "areas_for_improvement": ["Fluency", "Grammar complexity"],
                "next_level_readiness": "Ready for intermediate+"
            }
        }
        
        return {
            "success": True,
            "data": comprehensive_insights,
            "insight_confidence": 0.91,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Comprehensive insights generation failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
