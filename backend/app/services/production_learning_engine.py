
import asyncio
import logging
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime, timedelta
import numpy as np
from dataclasses import dataclass, asdict
from enum import Enum
import json
from .real_ai_models import real_ai_models, RealTimeAnalysis, LanguageLevel

logger = logging.getLogger(__name__)

class LearningObjective(Enum):
    FLUENCY = "fluency"
    ACCURACY = "accuracy"
    VOCABULARY = "vocabulary"
    PRONUNCIATION = "pronunciation"
    GRAMMAR = "grammar"
    CONFIDENCE = "confidence"

@dataclass
class LearningOutcome:
    objective: LearningObjective
    current_level: float
    target_level: float
    progress_rate: float
    estimated_completion: datetime
    action_plan: List[str]

@dataclass
class StudentProfile:
    user_id: str
    current_level: LanguageLevel
    learning_objectives: List[LearningObjective]
    strengths: List[str]
    weaknesses: List[str]
    learning_style: str
    motivation_level: float
    consistency_score: float
    time_invested: int  # em minutos
    last_activity: datetime

class ProductionLearningEngine:
    """
    Engine de aprendizado para produção focado em resultados reais
    Baseado em metodologias comprovadas de ensino de idiomas
    """
    
    def __init__(self):
        self.student_profiles = {}
        self.learning_pathways = {}
        self.performance_metrics = {}
        self.adaptive_content = {}
        
    async def create_student_profile(self, user_id: str, initial_assessment: Dict) -> StudentProfile:
        """
        Criar perfil completo do estudante baseado em avaliação inicial
        """
        try:
            logger.info(f"🎯 Creating comprehensive student profile for: {user_id}")
            
            # Analisar avaliação inicial
            level_assessment = self._assess_initial_level(initial_assessment)
            
            # Identificar objetivos de aprendizado
            learning_objectives = self._identify_learning_objectives(initial_assessment)
            
            # Análise de pontos fortes e fracos
            strengths, weaknesses = self._analyze_strengths_weaknesses(initial_assessment)
            
            # Identificar estilo de aprendizado
            learning_style = self._identify_learning_style(initial_assessment)
            
            # Criar perfil
            profile = StudentProfile(
                user_id=user_id,
                current_level=level_assessment,
                learning_objectives=learning_objectives,
                strengths=strengths,
                weaknesses=weaknesses,
                learning_style=learning_style,
                motivation_level=0.8,  # Initial high motivation
                consistency_score=0.0,  # No data yet
                time_invested=0,
                last_activity=datetime.now()
            )
            
            # Armazenar perfil
            self.student_profiles[user_id] = profile
            
            # Criar pathway personalizado
            await self._create_personalized_pathway(profile)
            
            logger.info(f"✅ Student profile created successfully for {user_id}")
            return profile
            
        except Exception as e:
            logger.error(f"Failed to create student profile: {e}")
            raise

    async def analyze_learning_session(self, user_id: str, session_data: Dict) -> Dict:
        """
        Analisar sessão de aprendizado em tempo real
        """
        try:
            profile = self.student_profiles.get(user_id)
            if not profile:
                raise ValueError(f"No profile found for user {user_id}")
            
            # Analisar performance na sessão
            session_analysis = self._analyze_session_performance(session_data)
            
            # Atualizar perfil do estudante
            await self._update_student_profile(user_id, session_analysis)
            
            # Gerar feedback personalizado
            feedback = self._generate_personalized_feedback(profile, session_analysis)
            
            # Ajustar dificuldade para próxima sessão
            next_difficulty = self._calculate_adaptive_difficulty(profile, session_analysis)
            
            # Recomendar próximas atividades
            next_activities = await self._recommend_next_activities(profile, session_analysis)
            
            return {
                "session_analysis": session_analysis,
                "personalized_feedback": feedback,
                "next_difficulty": next_difficulty,
                "recommended_activities": next_activities,
                "progress_update": self._calculate_progress_update(profile, session_analysis),
                "motivational_message": self._generate_motivational_message(profile, session_analysis)
            }
            
        except Exception as e:
            logger.error(f"Learning session analysis failed: {e}")
            raise

    async def generate_adaptive_lesson(self, user_id: str, lesson_type: str) -> Dict:
        """
        Gerar lição adaptativa baseada no perfil do estudante
        """
        try:
            profile = self.student_profiles.get(user_id)
            if not profile:
                raise ValueError(f"No profile found for user {user_id}")
            
            # Selecionar conteúdo baseado no perfil
            content = self._select_adaptive_content(profile, lesson_type)
            
            # Ajustar dificuldade
            difficulty = self._calculate_lesson_difficulty(profile, lesson_type)
            
            # Gerar exercícios personalizados
            exercises = await self._generate_personalized_exercises(profile, lesson_type, difficulty)
            
            # Criar plano de lição
            lesson_plan = {
                "lesson_id": f"{user_id}_{lesson_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "title": self._generate_lesson_title(profile, lesson_type),
                "objectives": self._define_lesson_objectives(profile, lesson_type),
                "content": content,
                "exercises": exercises,
                "difficulty_level": difficulty,
                "estimated_duration": self._estimate_lesson_duration(profile, exercises),
                "success_criteria": self._define_success_criteria(profile, lesson_type),
                "adaptive_hints": self._generate_adaptive_hints(profile, lesson_type)
            }
            
            return lesson_plan
            
        except Exception as e:
            logger.error(f"Adaptive lesson generation failed: {e}")
            raise

    async def track_learning_progress(self, user_id: str) -> Dict:
        """
        Rastrear progresso de aprendizado com métricas detalhadas
        """
        try:
            profile = self.student_profiles.get(user_id)
            if not profile:
                raise ValueError(f"No profile found for user {user_id}")
            
            # Calcular métricas de progresso
            progress_metrics = self._calculate_progress_metrics(profile)
            
            # Analisar tendências
            trends = self._analyze_learning_trends(user_id)
            
            # Calcular outcomes por objetivo
            outcomes = self._calculate_learning_outcomes(profile)
            
            # Gerar insights
            insights = self._generate_learning_insights(profile, trends)
            
            # Predições de sucesso
            predictions = self._predict_learning_success(profile, trends)
            
            return {
                "progress_metrics": progress_metrics,
                "learning_trends": trends,
                "objective_outcomes": outcomes,
                "insights": insights,
                "success_predictions": predictions,
                "milestone_progress": self._calculate_milestone_progress(profile),
                "time_to_fluency": self._estimate_time_to_fluency(profile, trends)
            }
            
        except Exception as e:
            logger.error(f"Learning progress tracking failed: {e}")
            raise

    def _assess_initial_level(self, assessment: Dict) -> LanguageLevel:
        """Avaliar nível inicial do estudante"""
        scores = assessment.get("scores", {})
        
        # Calcular score médio
        avg_score = np.mean(list(scores.values())) if scores else 0.5
        
        # Mapear para nível
        if avg_score >= 0.9:
            return LanguageLevel.C2
        elif avg_score >= 0.8:
            return LanguageLevel.C1
        elif avg_score >= 0.7:
            return LanguageLevel.B2
        elif avg_score >= 0.6:
            return LanguageLevel.B1
        elif avg_score >= 0.5:
            return LanguageLevel.A2
        else:
            return LanguageLevel.A1

    def _identify_learning_objectives(self, assessment: Dict) -> List[LearningObjective]:
        """Identificar objetivos de aprendizado baseado na avaliação"""
        objectives = []
        goals = assessment.get("goals", [])
        
        # Mapear goals para objectives
        goal_mapping = {
            "speak_fluently": LearningObjective.FLUENCY,
            "improve_pronunciation": LearningObjective.PRONUNCIATION,
            "expand_vocabulary": LearningObjective.VOCABULARY,
            "master_grammar": LearningObjective.GRAMMAR,
            "build_confidence": LearningObjective.CONFIDENCE,
            "speak_accurately": LearningObjective.ACCURACY
        }
        
        for goal in goals:
            if goal in goal_mapping:
                objectives.append(goal_mapping[goal])
        
        # Adicionar objectives baseado em scores baixos
        scores = assessment.get("scores", {})
        for skill, score in scores.items():
            if score < 0.6:
                if skill == "pronunciation":
                    objectives.append(LearningObjective.PRONUNCIATION)
                elif skill == "vocabulary":
                    objectives.append(LearningObjective.VOCABULARY)
                elif skill == "grammar":
                    objectives.append(LearningObjective.GRAMMAR)
        
        return list(set(objectives))  # Remove duplicates

    def _analyze_strengths_weaknesses(self, assessment: Dict) -> Tuple[List[str], List[str]]:
        """Analisar pontos fortes e fracos"""
        scores = assessment.get("scores", {})
        
        strengths = []
        weaknesses = []
        
        for skill, score in scores.items():
            if score >= 0.8:
                strengths.append(skill)
            elif score < 0.6:
                weaknesses.append(skill)
        
        return strengths, weaknesses

    def _identify_learning_style(self, assessment: Dict) -> str:
        """Identificar estilo de aprendizado"""
        preferences = assessment.get("preferences", {})
        
        if preferences.get("visual_learner", False):
            return "visual"
        elif preferences.get("auditory_learner", False):
            return "auditory"
        elif preferences.get("kinesthetic_learner", False):
            return "kinesthetic"
        else:
            return "mixed"

    async def _create_personalized_pathway(self, profile: StudentProfile):
        """Criar pathway personalizado de aprendizado"""
        pathway = {
            "user_id": profile.user_id,
            "current_level": profile.current_level.value,
            "target_level": self._calculate_target_level(profile),
            "learning_path": self._generate_learning_path(profile),
            "milestones": self._define_milestones(profile),
            "estimated_duration": self._estimate_pathway_duration(profile)
        }
        
        self.learning_pathways[profile.user_id] = pathway

    def _calculate_target_level(self, profile: StudentProfile) -> str:
        """Calcular nível target baseado nos objetivos"""
        objectives = profile.learning_objectives
        
        if LearningObjective.FLUENCY in objectives:
            return "C1"
        elif LearningObjective.ACCURACY in objectives:
            return "B2"
        else:
            # Próximo nível
            current_levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
            current_index = current_levels.index(profile.current_level.value)
            return current_levels[min(current_index + 1, len(current_levels) - 1)]

    def _generate_learning_path(self, profile: StudentProfile) -> List[Dict]:
        """Gerar caminho de aprendizado personalizado"""
        path = []
        
        # Focar nas fraquezas primeiro
        for weakness in profile.weaknesses:
            path.append({
                "phase": f"strengthen_{weakness}",
                "focus": weakness,
                "duration_weeks": 4,
                "activities": self._get_activities_for_skill(weakness)
            })
        
        # Depois trabalhar nos objetivos
        for objective in profile.learning_objectives:
            path.append({
                "phase": f"develop_{objective.value}",
                "focus": objective.value,
                "duration_weeks": 6,
                "activities": self._get_activities_for_objective(objective)
            })
        
        return path

    def _define_milestones(self, profile: StudentProfile) -> List[Dict]:
        """Definir marcos de progresso"""
        milestones = []
        
        # Marcos baseados em nível
        levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
        current_index = levels.index(profile.current_level.value)
        
        for i in range(current_index + 1, len(levels)):
            milestones.append({
                "level": levels[i],
                "description": f"Achieve {levels[i]} proficiency",
                "criteria": self._get_level_criteria(levels[i]),
                "estimated_weeks": (i - current_index) * 12
            })
        
        return milestones

    def _estimate_pathway_duration(self, profile: StudentProfile) -> int:
        """Estimar duração do pathway em semanas"""
        base_duration = 24  # 6 meses
        
        # Ajustar baseado no número de fraquezas
        weakness_penalty = len(profile.weaknesses) * 4
        
        # Ajustar baseado no número de objetivos
        objective_bonus = len(profile.learning_objectives) * 2
        
        return base_duration + weakness_penalty + objective_bonus

    def _analyze_session_performance(self, session_data: Dict) -> Dict:
        """Analisar performance na sessão"""
        performance = {
            "accuracy": session_data.get("accuracy", 0.0),
            "fluency": session_data.get("fluency", 0.0),
            "completion_rate": session_data.get("completion_rate", 0.0),
            "time_spent": session_data.get("time_spent", 0),
            "errors": session_data.get("errors", []),
            "improvements": session_data.get("improvements", []),
            "engagement_level": self._calculate_engagement_level(session_data)
        }
        
        return performance

    async def _update_student_profile(self, user_id: str, session_analysis: Dict):
        """Atualizar perfil do estudante baseado na sessão"""
        profile = self.student_profiles[user_id]
        
        # Atualizar tempo investido
        profile.time_invested += session_analysis.get("time_spent", 0)
        
        # Atualizar última atividade
        profile.last_activity = datetime.now()
        
        # Atualizar nível de motivação
        profile.motivation_level = self._update_motivation_level(
            profile.motivation_level, session_analysis
        )
        
        # Atualizar score de consistência
        profile.consistency_score = self._update_consistency_score(profile)

    def _generate_personalized_feedback(self, profile: StudentProfile, 
                                      session_analysis: Dict) -> List[str]:
        """Gerar feedback personalizado"""
        feedback = []
        
        accuracy = session_analysis.get("accuracy", 0.0)
        fluency = session_analysis.get("fluency", 0.0)
        
        # Feedback baseado em performance
        if accuracy >= 0.8:
            feedback.append("Excellent accuracy! You're really improving.")
        elif accuracy >= 0.6:
            feedback.append("Good accuracy. Keep practicing to reach the next level.")
        else:
            feedback.append("Focus on accuracy. Take your time with each answer.")
        
        if fluency >= 0.8:
            feedback.append("Great fluency! Your speaking is becoming more natural.")
        elif fluency >= 0.6:
            feedback.append("Good fluency development. Practice speaking regularly.")
        else:
            feedback.append("Work on fluency by practicing speaking every day.")
        
        # Feedback baseado em pontos fortes
        if "pronunciation" in profile.strengths:
            feedback.append("Your pronunciation strength is showing! Keep it up.")
        
        # Feedback baseado em fraquezas
        if "grammar" in profile.weaknesses:
            feedback.append("Continue working on grammar - it's getting better!")
        
        return feedback

    def _calculate_adaptive_difficulty(self, profile: StudentProfile, 
                                     session_analysis: Dict) -> str:
        """Calcular dificuldade adaptativa"""
        accuracy = session_analysis.get("accuracy", 0.0)
        completion_rate = session_analysis.get("completion_rate", 0.0)
        
        # Zona de desenvolvimento proximal
        if accuracy >= 0.9 and completion_rate >= 0.9:
            return "increase"  # Muito fácil
        elif accuracy < 0.5 or completion_rate < 0.5:
            return "decrease"  # Muito difícil
        else:
            return "maintain"  # Perfeito

    async def _recommend_next_activities(self, profile: StudentProfile, 
                                       session_analysis: Dict) -> List[Dict]:
        """Recomendar próximas atividades"""
        activities = []
        
        errors = session_analysis.get("errors", [])
        
        # Atividades baseadas em erros
        error_types = [error.get("type") for error in errors]
        
        if "pronunciation" in error_types:
            activities.append({
                "type": "pronunciation_practice",
                "focus": "error_correction",
                "duration": 10,
                "priority": "high"
            })
        
        if "grammar" in error_types:
            activities.append({
                "type": "grammar_drill",
                "focus": "error_patterns",
                "duration": 15,
                "priority": "medium"
            })
        
        # Atividades baseadas em objetivos
        for objective in profile.learning_objectives:
            if objective == LearningObjective.VOCABULARY:
                activities.append({
                    "type": "vocabulary_expansion",
                    "focus": "new_words",
                    "duration": 12,
                    "priority": "medium"
                })
        
        return activities

    def _calculate_progress_update(self, profile: StudentProfile, 
                                 session_analysis: Dict) -> Dict:
        """Calcular atualização de progresso"""
        return {
            "xp_gained": self._calculate_xp_gained(session_analysis),
            "streak_update": self._update_streak(profile),
            "level_progress": self._calculate_level_progress(profile, session_analysis),
            "objective_progress": self._calculate_objective_progress(profile, session_analysis)
        }

    def _generate_motivational_message(self, profile: StudentProfile, 
                                     session_analysis: Dict) -> str:
        """Gerar mensagem motivacional"""
        accuracy = session_analysis.get("accuracy", 0.0)
        
        if accuracy >= 0.9:
            return "🎉 Outstanding performance! You're mastering this!"
        elif accuracy >= 0.8:
            return "🌟 Great job! You're making excellent progress!"
        elif accuracy >= 0.7:
            return "👍 Good work! Keep pushing forward!"
        elif accuracy >= 0.6:
            return "💪 You're improving! Don't give up!"
        else:
            return "🎯 Every expert was once a beginner. Keep practicing!"

    def _calculate_engagement_level(self, session_data: Dict) -> float:
        """Calcular nível de engajamento"""
        time_spent = session_data.get("time_spent", 0)
        completion_rate = session_data.get("completion_rate", 0.0)
        
        # Engajamento baseado em tempo e completion
        if time_spent > 0 and completion_rate > 0:
            return min(1.0, (time_spent / 600) * completion_rate)  # 10 min ideal
        
        return 0.0

    def _update_motivation_level(self, current_motivation: float, 
                               session_analysis: Dict) -> float:
        """Atualizar nível de motivação"""
        accuracy = session_analysis.get("accuracy", 0.0)
        
        if accuracy >= 0.8:
            return min(1.0, current_motivation + 0.1)
        elif accuracy < 0.5:
            return max(0.1, current_motivation - 0.1)
        
        return current_motivation

    def _update_consistency_score(self, profile: StudentProfile) -> float:
        """Atualizar score de consistência"""
        # Implementar lógica de consistência baseada em histórico
        days_since_last = (datetime.now() - profile.last_activity).days
        
        if days_since_last == 0:
            return min(1.0, profile.consistency_score + 0.1)
        elif days_since_last == 1:
            return profile.consistency_score
        else:
            return max(0.0, profile.consistency_score - 0.1)

    def _get_activities_for_skill(self, skill: str) -> List[str]:
        """Obter atividades para uma habilidade específica"""
        activities_map = {
            "pronunciation": ["phonetic_drills", "minimal_pairs", "rhythm_practice"],
            "grammar": ["structure_drills", "error_correction", "pattern_practice"],
            "vocabulary": ["word_association", "contextual_usage", "collocations"],
            "listening": ["audio_comprehension", "dictation", "accent_training"],
            "speaking": ["conversation_practice", "monologue_tasks", "role_plays"]
        }
        
        return activities_map.get(skill, ["general_practice"])

    def _get_activities_for_objective(self, objective: LearningObjective) -> List[str]:
        """Obter atividades para um objetivo específico"""
        activities_map = {
            LearningObjective.FLUENCY: ["free_conversation", "storytelling", "debates"],
            LearningObjective.ACCURACY: ["precision_drills", "error_analysis", "self_correction"],
            LearningObjective.PRONUNCIATION: ["phonetic_training", "accent_reduction", "intonation"],
            LearningObjective.VOCABULARY: ["word_building", "semantic_mapping", "usage_practice"],
            LearningObjective.GRAMMAR: ["structure_analysis", "transformation_drills", "error_correction"],
            LearningObjective.CONFIDENCE: ["speaking_practice", "presentation_skills", "social_interaction"]
        }
        
        return activities_map.get(objective, ["general_practice"])

    def _get_level_criteria(self, level: str) -> List[str]:
        """Obter critérios para um nível específico"""
        criteria_map = {
            "A2": ["Express simple ideas clearly", "Use basic grammar correctly", "Understand common phrases"],
            "B1": ["Participate in conversations", "Express opinions", "Handle routine tasks"],
            "B2": ["Discuss complex topics", "Express ideas fluently", "Understand native speakers"],
            "C1": ["Express ideas spontaneously", "Use language flexibly", "Understand implicit meaning"],
            "C2": ["Express ideas effortlessly", "Master complex grammar", "Understand everything"]
        }
        
        return criteria_map.get(level, ["Continue practicing"])

    def _calculate_xp_gained(self, session_analysis: Dict) -> int:
        """Calcular XP ganho na sessão"""
        accuracy = session_analysis.get("accuracy", 0.0)
        completion_rate = session_analysis.get("completion_rate", 0.0)
        time_spent = session_analysis.get("time_spent", 0)
        
        base_xp = 100
        accuracy_bonus = int(accuracy * 50)
        completion_bonus = int(completion_rate * 30)
        time_bonus = min(20, time_spent // 60)  # 1 ponto por minuto, max 20
        
        return base_xp + accuracy_bonus + completion_bonus + time_bonus

    def _update_streak(self, profile: StudentProfile) -> int:
        """Atualizar streak do usuário"""
        # Implementar lógica de streak baseada em atividade diária
        days_since_last = (datetime.now() - profile.last_activity).days
        
        if days_since_last <= 1:
            return 1  # Manter ou aumentar streak
        else:
            return 0  # Quebrar streak

    def _calculate_level_progress(self, profile: StudentProfile, 
                                session_analysis: Dict) -> float:
        """Calcular progresso no nível atual"""
        accuracy = session_analysis.get("accuracy", 0.0)
        
        # Progresso baseado em performance
        progress_increment = accuracy * 0.05  # 5% do accuracy como progresso
        
        return progress_increment

    def _calculate_objective_progress(self, profile: StudentProfile, 
                                    session_analysis: Dict) -> Dict:
        """Calcular progresso nos objetivos"""
        objective_progress = {}
        
        for objective in profile.learning_objectives:
            if objective == LearningObjective.ACCURACY:
                objective_progress[objective.value] = session_analysis.get("accuracy", 0.0)
            elif objective == LearningObjective.FLUENCY:
                objective_progress[objective.value] = session_analysis.get("fluency", 0.0)
            else:
                objective_progress[objective.value] = 0.7  # Progresso padrão
        
        return objective_progress

    def _calculate_progress_metrics(self, profile: StudentProfile) -> Dict:
        """Calcular métricas de progresso"""
        return {
            "time_invested_hours": profile.time_invested / 60,
            "consistency_score": profile.consistency_score,
            "motivation_level": profile.motivation_level,
            "current_level": profile.current_level.value,
            "strengths_count": len(profile.strengths),
            "weaknesses_count": len(profile.weaknesses),
            "objectives_progress": self._calculate_objectives_progress(profile)
        }

    def _analyze_learning_trends(self, user_id: str) -> Dict:
        """Analisar tendências de aprendizado"""
        # Implementar análise de tendências baseada em histórico
        return {
            "accuracy_trend": "improving",
            "fluency_trend": "stable",
            "consistency_trend": "improving",
            "engagement_trend": "high",
            "difficulty_adaptation": "optimal"
        }

    def _calculate_learning_outcomes(self, profile: StudentProfile) -> List[LearningOutcome]:
        """Calcular outcomes de aprendizado"""
        outcomes = []
        
        for objective in profile.learning_objectives:
            outcome = LearningOutcome(
                objective=objective,
                current_level=0.6,  # Valor exemplo
                target_level=0.9,
                progress_rate=0.05,  # 5% por semana
                estimated_completion=datetime.now() + timedelta(weeks=6),
                action_plan=self._generate_action_plan(objective)
            )
            outcomes.append(outcome)
        
        return outcomes

    def _generate_action_plan(self, objective: LearningObjective) -> List[str]:
        """Gerar plano de ação para objetivo"""
        action_plans = {
            LearningObjective.FLUENCY: [
                "Practice speaking 15 minutes daily",
                "Record yourself speaking weekly",
                "Join conversation groups"
            ],
            LearningObjective.ACCURACY: [
                "Focus on grammar drills",
                "Practice error correction",
                "Review mistakes daily"
            ],
            LearningObjective.PRONUNCIATION: [
                "Practice phonetic exercises",
                "Record and compare pronunciation",
                "Work with minimal pairs"
            ]
        }
        
        return action_plans.get(objective, ["Continue regular practice"])

    def _generate_learning_insights(self, profile: StudentProfile, trends: Dict) -> List[str]:
        """Gerar insights de aprendizado"""
        insights = []
        
        if profile.consistency_score > 0.8:
            insights.append("Your consistency is excellent! This is key to success.")
        
        if profile.motivation_level > 0.8:
            insights.append("Your motivation is high - perfect for accelerated learning!")
        
        if len(profile.weaknesses) > len(profile.strengths):
            insights.append("Focus on strengthening weak areas for balanced improvement.")
        
        return insights

    def _predict_learning_success(self, profile: StudentProfile, trends: Dict) -> Dict:
        """Predizer sucesso de aprendizado"""
        success_factors = {
            "consistency": profile.consistency_score,
            "motivation": profile.motivation_level,
            "engagement": 0.8,  # Baseado em trends
            "time_investment": min(1.0, profile.time_invested / 3600)  # 60 hours ideal
        }
        
        overall_success_probability = np.mean(list(success_factors.values()))
        
        return {
            "success_probability": overall_success_probability,
            "key_factors": success_factors,
            "predicted_outcome": "successful" if overall_success_probability > 0.7 else "needs_improvement",
            "recommendations": self._generate_success_recommendations(success_factors)
        }

    def _generate_success_recommendations(self, factors: Dict) -> List[str]:
        """Gerar recomendações para sucesso"""
        recommendations = []
        
        if factors["consistency"] < 0.7:
            recommendations.append("Improve study consistency - aim for daily practice")
        
        if factors["motivation"] < 0.7:
            recommendations.append("Set small, achievable goals to boost motivation")
        
        if factors["time_investment"] < 0.5:
            recommendations.append("Increase study time - aim for 30+ minutes daily")
        
        return recommendations

    def _calculate_milestone_progress(self, profile: StudentProfile) -> Dict:
        """Calcular progresso em marcos"""
        pathway = self.learning_pathways.get(profile.user_id, {})
        milestones = pathway.get("milestones", [])
        
        progress = {}
        for milestone in milestones:
            # Simular progresso baseado em tempo investido
            progress[milestone["level"]] = min(1.0, profile.time_invested / (milestone["estimated_weeks"] * 7 * 60))
        
        return progress

    def _estimate_time_to_fluency(self, profile: StudentProfile, trends: Dict) -> Dict:
        """Estimar tempo para fluência"""
        base_hours = 1000  # Horas base para fluência
        
        # Ajustar baseado em fatores
        multiplier = 1.0
        
        if profile.consistency_score > 0.8:
            multiplier *= 0.8
        
        if profile.motivation_level > 0.8:
            multiplier *= 0.9
        
        if len(profile.strengths) > len(profile.weaknesses):
            multiplier *= 0.9
        
        estimated_hours = base_hours * multiplier
        hours_remaining = estimated_hours - profile.time_invested
        
        return {
            "estimated_total_hours": estimated_hours,
            "hours_remaining": max(0, hours_remaining),
            "months_remaining": max(0, hours_remaining / 30),  # 1 hora por dia
            "confidence_level": 0.85 if profile.consistency_score > 0.7 else 0.65
        }

    def _calculate_objectives_progress(self, profile: StudentProfile) -> Dict:
        """Calcular progresso nos objetivos"""
        progress = {}
        
        for objective in profile.learning_objectives:
            # Simular progresso baseado em tempo e performance
            progress[objective.value] = min(1.0, profile.time_invested / 1800)  # 30 horas por objetivo
        
        return progress

# Instância global
production_learning_engine = ProductionLearningEngine()
