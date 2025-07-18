
import asyncio
import logging
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import numpy as np
from dataclasses import dataclass
from enum import Enum
import json

logger = logging.getLogger(__name__)

class LearningStyle(Enum):
    VISUAL = "visual"
    AUDITORY = "auditory"
    KINESTHETIC = "kinesthetic"
    READING_WRITING = "reading_writing"

class DifficultyLevel(Enum):
    BEGINNER = "beginner"
    ELEMENTARY = "elementary"
    INTERMEDIATE = "intermediate"
    UPPER_INTERMEDIATE = "upper_intermediate"
    ADVANCED = "advanced"
    PROFICIENT = "proficient"

@dataclass
class LearningProgress:
    user_id: str
    current_level: DifficultyLevel
    learning_velocity: float
    retention_rate: float
    consistency_score: float
    weak_areas: List[str]
    strong_areas: List[str]
    optimal_session_length: int
    next_review_date: datetime

class AdvancedLearningEngine:
    """
    Motor de aprendizado avançado com IA adaptativa
    Sistema completo de personalização e otimização do aprendizado
    """
    
    def __init__(self):
        self.learning_profiles = {}
        self.content_difficulty_matrix = {}
        self.spaced_repetition_intervals = [1, 3, 7, 14, 30, 90, 180]
        
    async def analyze_learning_pattern(self, user_id: str, 
                                     performance_history: List[Dict]) -> Dict:
        """
        Análise avançada de padrões de aprendizado do usuário
        """
        try:
            logger.info(f"🧠 Analyzing learning patterns for user: {user_id}")
            
            if not performance_history:
                return self._create_default_learning_profile(user_id)
            
            # Análise de velocidade de aprendizado
            learning_velocity = self._calculate_learning_velocity(performance_history)
            
            # Análise de retenção
            retention_analysis = self._analyze_retention_patterns(performance_history)
            
            # Identificação de estilo de aprendizado
            learning_style = self._identify_learning_style(performance_history)
            
            # Análise de consistência
            consistency_score = self._calculate_consistency_score(performance_history)
            
            # Identificação de pontos fortes e fracos
            strengths_weaknesses = self._analyze_strengths_weaknesses(performance_history)
            
            # Predição de sucesso
            success_prediction = self._predict_learning_success(
                learning_velocity, retention_analysis, consistency_score
            )
            
            learning_profile = {
                "user_id": user_id,
                "learning_velocity": learning_velocity,
                "retention_rate": retention_analysis["overall_retention"],
                "learning_style": learning_style,
                "consistency_score": consistency_score,
                "optimal_session_length": self._calculate_optimal_session_length(performance_history),
                "peak_performance_hours": self._identify_peak_hours(performance_history),
                "weak_areas": strengths_weaknesses["weak_areas"],
                "strong_areas": strengths_weaknesses["strong_areas"],
                "success_prediction": success_prediction,
                "recommended_study_plan": self._generate_study_plan(
                    learning_velocity, retention_analysis, consistency_score
                ),
                "next_milestone": self._calculate_next_milestone(performance_history),
                "estimated_fluency_date": self._estimate_fluency_timeline(
                    learning_velocity, retention_analysis
                )
            }
            
            # Cache do perfil
            self.learning_profiles[user_id] = learning_profile
            
            return learning_profile
            
        except Exception as e:
            logger.error(f"Learning pattern analysis failed: {e}")
            return self._create_default_learning_profile(user_id)
    
    async def generate_adaptive_content(self, user_id: str, 
                                      lesson_type: str) -> Dict:
        """
        Geração de conteúdo adaptativo baseado no perfil do usuário
        """
        try:
            logger.info(f"📚 Generating adaptive content for user: {user_id}")
            
            # Obter perfil de aprendizado
            profile = self.learning_profiles.get(user_id)
            if not profile:
                profile = await self.analyze_learning_pattern(user_id, [])
            
            # Ajustar dificuldade dinamicamente
            optimal_difficulty = self._calculate_optimal_difficulty(profile)
            
            # Gerar conteúdo personalizado
            adaptive_content = {
                "lesson_id": f"adaptive_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "difficulty_level": optimal_difficulty,
                "content_type": self._select_optimal_content_type(profile),
                "exercises": self._generate_personalized_exercises(profile, lesson_type),
                "focus_areas": profile["weak_areas"][:3],
                "estimated_completion_time": profile["optimal_session_length"],
                "spaced_repetition_items": self._get_spaced_repetition_items(user_id),
                "gamification_elements": self._add_gamification_elements(profile),
                "success_probability": self._predict_exercise_success(profile, optimal_difficulty)
            }
            
            return adaptive_content
            
        except Exception as e:
            logger.error(f"Adaptive content generation failed: {e}")
            return {"error": str(e)}
    
    async def optimize_learning_path(self, user_id: str) -> Dict:
        """
        Otimização do caminho de aprendizado usando IA
        """
        try:
            logger.info(f"🎯 Optimizing learning path for user: {user_id}")
            
            profile = self.learning_profiles.get(user_id, {})
            
            # Análise de lacunas de conhecimento
            knowledge_gaps = self._identify_knowledge_gaps(profile)
            
            # Otimização de sequência de aprendizado
            optimized_sequence = self._optimize_learning_sequence(knowledge_gaps, profile)
            
            # Cronograma personalizado
            personalized_schedule = self._create_personalized_schedule(profile)
            
            # Metas adaptativas
            adaptive_goals = self._set_adaptive_goals(profile)
            
            optimization_plan = {
                "current_level": profile.get("current_level", "intermediate"),
                "knowledge_gaps": knowledge_gaps,
                "optimized_learning_sequence": optimized_sequence,
                "personalized_schedule": personalized_schedule,
                "adaptive_goals": adaptive_goals,
                "milestone_timeline": self._create_milestone_timeline(profile),
                "intervention_points": self._identify_intervention_points(profile),
                "motivation_strategies": self._recommend_motivation_strategies(profile)
            }
            
            return optimization_plan
            
        except Exception as e:
            logger.error(f"Learning path optimization failed: {e}")
            return {"error": str(e)}
    
    async def provide_real_time_coaching(self, user_id: str, 
                                       current_performance: Dict) -> Dict:
        """
        Coaching em tempo real baseado em performance atual
        """
        try:
            logger.info(f"🎓 Providing real-time coaching for user: {user_id}")
            
            profile = self.learning_profiles.get(user_id, {})
            
            # Análise da performance atual
            performance_analysis = self._analyze_current_performance(
                current_performance, profile
            )
            
            # Feedback imediato personalizado
            immediate_feedback = self._generate_immediate_feedback(
                performance_analysis, profile
            )
            
            # Ajustes dinâmicos
            dynamic_adjustments = self._suggest_dynamic_adjustments(
                performance_analysis, profile
            )
            
            # Motivação contextual
            contextual_motivation = self._provide_contextual_motivation(
                performance_analysis, profile
            )
            
            coaching_response = {
                "immediate_feedback": immediate_feedback,
                "performance_trend": performance_analysis["trend"],
                "confidence_level": performance_analysis["confidence"],
                "dynamic_adjustments": dynamic_adjustments,
                "contextual_motivation": contextual_motivation,
                "next_action": self._recommend_next_action(performance_analysis),
                "learning_tip": self._provide_contextual_tip(performance_analysis, profile),
                "progress_celebration": self._generate_progress_celebration(performance_analysis)
            }
            
            return coaching_response
            
        except Exception as e:
            logger.error(f"Real-time coaching failed: {e}")
            return {"error": str(e)}
    
    # Métodos auxiliares para análise de aprendizado
    def _calculate_learning_velocity(self, performance_history: List[Dict]) -> float:
        """Calcula velocidade de aprendizado"""
        if len(performance_history) < 2:
            return 0.5
        
        scores = [p.get("score", 0) for p in performance_history[-10:]]
        if len(scores) < 2:
            return 0.5
        
        # Calcular tendência de melhoria
        x = np.arange(len(scores))
        slope = np.polyfit(x, scores, 1)[0]
        
        # Normalizar para 0-1
        normalized_velocity = max(0, min(1, (slope + 10) / 20))
        return normalized_velocity
    
    def _analyze_retention_patterns(self, performance_history: List[Dict]) -> Dict:
        """Analisa padrões de retenção"""
        retention_data = {
            "overall_retention": 0.75,
            "short_term_retention": 0.85,
            "long_term_retention": 0.65,
            "retention_decay_rate": 0.1
        }
        
        if len(performance_history) > 5:
            recent_scores = [p.get("score", 0) for p in performance_history[-5:]]
            older_scores = [p.get("score", 0) for p in performance_history[-10:-5]]
            
            if older_scores and recent_scores:
                retention_data["overall_retention"] = np.mean(recent_scores) / max(np.mean(older_scores), 1)
                retention_data["overall_retention"] = min(1.0, retention_data["overall_retention"])
        
        return retention_data
    
    def _identify_learning_style(self, performance_history: List[Dict]) -> str:
        """Identifica estilo de aprendizado preferido"""
        # Análise baseada em tipos de exercícios com melhor performance
        style_scores = {
            "visual": 0,
            "auditory": 0,
            "kinesthetic": 0,
            "reading_writing": 0
        }
        
        for performance in performance_history:
            exercise_type = performance.get("exercise_type", "mixed")
            score = performance.get("score", 0)
            
            if "visual" in exercise_type or "image" in exercise_type:
                style_scores["visual"] += score
            elif "audio" in exercise_type or "listening" in exercise_type:
                style_scores["auditory"] += score
            elif "interactive" in exercise_type or "game" in exercise_type:
                style_scores["kinesthetic"] += score
            else:
                style_scores["reading_writing"] += score
        
        return max(style_scores, key=style_scores.get)
    
    def _calculate_consistency_score(self, performance_history: List[Dict]) -> float:
        """Calcula score de consistência"""
        if len(performance_history) < 3:
            return 0.5
        
        scores = [p.get("score", 0) for p in performance_history[-10:]]
        consistency = 1 - (np.std(scores) / 100)
        return max(0, min(1, consistency))
    
    def _analyze_strengths_weaknesses(self, performance_history: List[Dict]) -> Dict:
        """Analisa pontos fortes e fracos"""
        skill_performance = {}
        
        for performance in performance_history:
            skills = performance.get("skills_tested", ["general"])
            score = performance.get("score", 0)
            
            for skill in skills:
                if skill not in skill_performance:
                    skill_performance[skill] = []
                skill_performance[skill].append(score)
        
        # Calcular médias por habilidade
        skill_averages = {
            skill: np.mean(scores) 
            for skill, scores in skill_performance.items()
        }
        
        # Identificar pontos fortes (acima de 80) e fracos (abaixo de 60)
        strong_areas = [skill for skill, avg in skill_averages.items() if avg > 80]
        weak_areas = [skill for skill, avg in skill_averages.items() if avg < 60]
        
        return {
            "strong_areas": strong_areas,
            "weak_areas": weak_areas,
            "skill_averages": skill_averages
        }
    
    def _predict_learning_success(self, velocity: float, retention: Dict, 
                                consistency: float) -> Dict:
        """Prediz sucesso no aprendizado"""
        # Algoritmo de predição baseado em múltiplos fatores
        success_score = (
            velocity * 0.3 + 
            retention["overall_retention"] * 0.4 + 
            consistency * 0.3
        )
        
        confidence = min(0.95, 0.6 + (consistency * 0.4))
        
        return {
            "success_probability": success_score,
            "confidence": confidence,
            "predicted_timeline": "3-6 months" if success_score > 0.7 else "6-12 months",
            "risk_factors": self._identify_risk_factors(velocity, retention, consistency)
        }
    
    def _calculate_optimal_session_length(self, performance_history: List[Dict]) -> int:
        """Calcula duração ótima de sessão"""
        if not performance_history:
            return 15
        
        # Análise baseada em performance vs duração
        durations = []
        scores = []
        
        for performance in performance_history:
            if "duration" in performance and "score" in performance:
                durations.append(performance["duration"])
                scores.append(performance["score"])
        
        if len(durations) < 3:
            return 15
        
        # Encontrar duração com melhor performance média
        duration_performance = {}
        for i, duration in enumerate(durations):
            duration_range = (duration // 5) * 5  # Agrupar em intervalos de 5 min
            if duration_range not in duration_performance:
                duration_performance[duration_range] = []
            duration_performance[duration_range].append(scores[i])
        
        best_duration = max(
            duration_performance.items(),
            key=lambda x: np.mean(x[1])
        )[0]
        
        return max(10, min(30, best_duration))
    
    def _identify_peak_hours(self, performance_history: List[Dict]) -> List[int]:
        """Identifica horários de pico de performance"""
        hour_performance = {}
        
        for performance in performance_history:
            timestamp = performance.get("timestamp")
            if timestamp:
                hour = datetime.fromisoformat(timestamp.replace('Z', '+00:00')).hour
                score = performance.get("score", 0)
                
                if hour not in hour_performance:
                    hour_performance[hour] = []
                hour_performance[hour].append(score)
        
        # Calcular médias por hora
        hour_averages = {
            hour: np.mean(scores)
            for hour, scores in hour_performance.items()
            if len(scores) >= 2
        }
        
        if not hour_averages:
            return [9, 14, 19]  # Horários padrão
        
        # Retornar top 3 horários
        sorted_hours = sorted(hour_averages.items(), key=lambda x: x[1], reverse=True)
        return [hour for hour, _ in sorted_hours[:3]]
    
    def _create_default_learning_profile(self, user_id: str) -> Dict:
        """Cria perfil padrão para novos usuários"""
        return {
            "user_id": user_id,
            "learning_velocity": 0.5,
            "retention_rate": 0.75,
            "learning_style": "mixed",
            "consistency_score": 0.5,
            "optimal_session_length": 15,
            "peak_performance_hours": [9, 14, 19],
            "weak_areas": ["pronunciation", "grammar"],
            "strong_areas": ["vocabulary"],
            "success_prediction": {
                "success_probability": 0.7,
                "confidence": 0.6,
                "predicted_timeline": "6-9 months"
            }
        }
    
    def _calculate_optimal_difficulty(self, profile: Dict) -> str:
        """Calcula dificuldade ótima baseada no perfil"""
        success_prob = profile.get("success_prediction", {}).get("success_probability", 0.7)
        learning_velocity = profile.get("learning_velocity", 0.5)
        
        if success_prob > 0.8 and learning_velocity > 0.7:
            return "challenging"
        elif success_prob > 0.6 and learning_velocity > 0.5:
            return "moderate"
        else:
            return "comfortable"
    
    def _select_optimal_content_type(self, profile: Dict) -> str:
        """Seleciona tipo de conteúdo ótimo"""
        learning_style = profile.get("learning_style", "mixed")
        
        style_content_map = {
            "visual": "interactive_visuals",
            "auditory": "audio_intensive",
            "kinesthetic": "gamified_practice",
            "reading_writing": "text_based",
            "mixed": "multimedia"
        }
        
        return style_content_map.get(learning_style, "multimedia")
    
    def _generate_personalized_exercises(self, profile: Dict, lesson_type: str) -> List[Dict]:
        """Gera exercícios personalizados"""
        weak_areas = profile.get("weak_areas", [])
        learning_style = profile.get("learning_style", "mixed")
        
        exercises = []
        
        # Exercícios focados em áreas fracas
        for area in weak_areas[:2]:
            exercises.append({
                "type": f"{area}_practice",
                "difficulty": "adaptive",
                "style": learning_style,
                "duration": 5,
                "importance": "high"
            })
        
        # Exercícios de reforço
        exercises.append({
            "type": "mixed_review",
            "difficulty": "moderate",
            "style": learning_style,
            "duration": 8,
            "importance": "medium"
        })
        
        return exercises
    
    def _get_spaced_repetition_items(self, user_id: str) -> List[Dict]:
        """Obtém itens para repetição espaçada"""
        # Em produção, buscar do banco de dados
        return [
            {
                "content": "Past tense irregular verbs",
                "next_review": datetime.now() + timedelta(days=3),
                "interval": 3,
                "importance": "high"
            },
            {
                "content": "Pronunciation: /th/ sound",
                "next_review": datetime.now() + timedelta(days=1),
                "interval": 1,
                "importance": "medium"
            }
        ]
    
    def _add_gamification_elements(self, profile: Dict) -> Dict:
        """Adiciona elementos de gamificação"""
        return {
            "challenges": ["Daily pronunciation challenge", "Grammar streak"],
            "rewards": ["New badge available", "XP bonus"],
            "competitions": ["Weekly leaderboard", "Friend challenges"],
            "achievements": ["Consistency master", "Pronunciation pro"]
        }
    
    def _predict_exercise_success(self, profile: Dict, difficulty: str) -> float:
        """Prediz sucesso no exercício"""
        base_success = profile.get("success_prediction", {}).get("success_probability", 0.7)
        
        difficulty_modifiers = {
            "comfortable": 0.1,
            "moderate": 0.0,
            "challenging": -0.1
        }
        
        modifier = difficulty_modifiers.get(difficulty, 0.0)
        return max(0.1, min(0.95, base_success + modifier))

# Global instance
advanced_learning_engine = AdvancedLearningEngine()
