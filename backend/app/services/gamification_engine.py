
import asyncio
import logging
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum
import json

logger = logging.getLogger(__name__)

class AchievementType(Enum):
    CONSISTENCY = "consistency"
    IMPROVEMENT = "improvement"
    MILESTONE = "milestone"
    SOCIAL = "social"
    MASTERY = "mastery"

class BadgeRarity(Enum):
    COMMON = "common"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"

@dataclass
class Achievement:
    id: str
    name: str
    description: str
    badge_rarity: BadgeRarity
    xp_reward: int
    criteria: Dict
    unlock_message: str

class GamificationEngine:
    """
    Sistema avançado de gamificação para o Bilingui-AI
    Controla XP, achievements, streaks, leaderboards e motivação
    """
    
    def __init__(self):
        self.achievements_catalog = self._initialize_achievements()
        self.user_stats = {}
        self.leaderboards = {}
        
    def _initialize_achievements(self) -> Dict[str, Achievement]:
        """Inicializa catálogo de achievements"""
        achievements = {
            # Achievements de Consistência
            "first_lesson": Achievement(
                id="first_lesson",
                name="First Steps",
                description="Complete your first lesson",
                badge_rarity=BadgeRarity.COMMON,
                xp_reward=50,
                criteria={"lessons_completed": 1},
                unlock_message="🎉 Welcome to your language journey!"
            ),
            "streak_3": Achievement(
                id="streak_3",
                name="Getting Started",
                description="Maintain a 3-day learning streak",
                badge_rarity=BadgeRarity.COMMON,
                xp_reward=100,
                criteria={"streak_days": 3},
                unlock_message="🔥 You're building momentum!"
            ),
            "streak_7": Achievement(
                id="streak_7",
                name="Weekly Warrior",
                description="Maintain a 7-day learning streak",
                badge_rarity=BadgeRarity.RARE,
                xp_reward=250,
                criteria={"streak_days": 7},
                unlock_message="⚡ One week of dedication!"
            ),
            "streak_30": Achievement(
                id="streak_30",
                name="Monthly Master",
                description="Maintain a 30-day learning streak",
                badge_rarity=BadgeRarity.EPIC,
                xp_reward=1000,
                criteria={"streak_days": 30},
                unlock_message="🏆 Incredible consistency!"
            ),
            "streak_100": Achievement(
                id="streak_100",
                name="Century Champion",
                description="Maintain a 100-day learning streak",
                badge_rarity=BadgeRarity.LEGENDARY,
                xp_reward=5000,
                criteria={"streak_days": 100},
                unlock_message="👑 You are unstoppable!"
            ),
            
            # Achievements de Melhoria
            "pronunciation_pro": Achievement(
                id="pronunciation_pro",
                name="Pronunciation Pro",
                description="Score 90+ on pronunciation 10 times",
                badge_rarity=BadgeRarity.RARE,
                xp_reward=300,
                criteria={"pronunciation_scores_90_plus": 10},
                unlock_message="🎤 Your pronunciation is excellent!"
            ),
            "fluency_master": Achievement(
                id="fluency_master",
                name="Fluency Master",
                description="Achieve 95+ fluency score",
                badge_rarity=BadgeRarity.EPIC,
                xp_reward=500,
                criteria={"max_fluency_score": 95},
                unlock_message="🌟 You speak like a native!"
            ),
            
            # Achievements de Marco
            "level_up": Achievement(
                id="level_up",
                name="Level Up",
                description="Reach level 10",
                badge_rarity=BadgeRarity.RARE,
                xp_reward=400,
                criteria={"level": 10},
                unlock_message="📈 You've leveled up significantly!"
            ),
            "xp_collector": Achievement(
                id="xp_collector",
                name="XP Collector",
                description="Earn 10,000 total XP",
                badge_rarity=BadgeRarity.EPIC,
                xp_reward=1000,
                criteria={"total_xp": 10000},
                unlock_message="💎 You're a dedicated learner!"
            ),
            
            # Achievements Sociais
            "helpful_friend": Achievement(
                id="helpful_friend",
                name="Helpful Friend",
                description="Help 5 friends with practice",
                badge_rarity=BadgeRarity.RARE,
                xp_reward=300,
                criteria={"friends_helped": 5},
                unlock_message="🤝 You're a great learning partner!"
            ),
            "community_leader": Achievement(
                id="community_leader",
                name="Community Leader",
                description="Be in top 10 on leaderboard for 7 days",
                badge_rarity=BadgeRarity.EPIC,
                xp_reward=750,
                criteria={"leaderboard_top10_days": 7},
                unlock_message="🥇 You inspire others!"
            ),
            
            # Achievements de Maestria
            "grammar_guru": Achievement(
                id="grammar_guru",
                name="Grammar Guru",
                description="Perfect grammar score in 20 exercises",
                badge_rarity=BadgeRarity.EPIC,
                xp_reward=600,
                criteria={"perfect_grammar_scores": 20},
                unlock_message="📚 Your grammar is impeccable!"
            ),
            "conversation_champion": Achievement(
                id="conversation_champion",
                name="Conversation Champion",
                description="Complete 50 conversation exercises",
                badge_rarity=BadgeRarity.EPIC,
                xp_reward=800,
                criteria={"conversation_exercises": 50},
                unlock_message="💬 You're a conversation expert!"
            )
        }
        
        return achievements
    
    async def calculate_xp_reward(self, activity_type: str, performance_data: Dict,
                                user_id: str) -> Dict:
        """
        Calcula recompensa XP baseada na atividade e performance
        """
        try:
            logger.info(f"🎯 Calculating XP reward for user: {user_id}")
            
            base_xp = self._get_base_xp(activity_type)
            performance_multiplier = self._calculate_performance_multiplier(performance_data)
            consistency_bonus = await self._calculate_consistency_bonus(user_id)
            streak_multiplier = await self._get_streak_multiplier(user_id)
            
            # Cálculo final do XP
            total_xp = int(base_xp * performance_multiplier * streak_multiplier) + consistency_bonus
            
            # Bonus especiais
            special_bonuses = await self._check_special_bonuses(user_id, activity_type, performance_data)
            
            xp_breakdown = {
                "base_xp": base_xp,
                "performance_multiplier": performance_multiplier,
                "streak_multiplier": streak_multiplier,
                "consistency_bonus": consistency_bonus,
                "special_bonuses": special_bonuses,
                "total_xp": total_xp + sum(special_bonuses.values()),
                "activity_type": activity_type,
                "calculation_details": {
                    "performance_score": performance_data.get("score", 0),
                    "time_spent": performance_data.get("duration", 0),
                    "difficulty": performance_data.get("difficulty", "medium")
                }
            }
            
            return xp_breakdown
            
        except Exception as e:
            logger.error(f"XP calculation failed: {e}")
            return {"total_xp": 10, "error": str(e)}
    
    async def check_achievements(self, user_id: str, user_stats: Dict) -> List[Dict]:
        """
        Verifica achievements desbloqueados
        """
        try:
            logger.info(f"🏆 Checking achievements for user: {user_id}")
            
            unlocked_achievements = []
            
            for achievement_id, achievement in self.achievements_catalog.items():
                if await self._is_achievement_unlocked(achievement, user_stats):
                    if not await self._user_has_achievement(user_id, achievement_id):
                        unlocked_achievements.append({
                            "achievement": achievement,
                            "unlocked_at": datetime.now().isoformat(),
                            "celebration_data": self._create_celebration_data(achievement)
                        })
            
            return unlocked_achievements
            
        except Exception as e:
            logger.error(f"Achievement check failed: {e}")
            return []
    
    async def update_streak(self, user_id: str, activity_date: datetime = None) -> Dict:
        """
        Atualiza streak do usuário
        """
        try:
            logger.info(f"🔥 Updating streak for user: {user_id}")
            
            if not activity_date:
                activity_date = datetime.now()
            
            # Buscar streak atual (em produção, do banco de dados)
            current_streak = await self._get_current_streak(user_id)
            last_activity = await self._get_last_activity_date(user_id)
            
            # Calcular novo streak
            new_streak_data = self._calculate_new_streak(
                current_streak, last_activity, activity_date
            )
            
            # Verificar records pessoais
            personal_records = await self._check_personal_records(user_id, new_streak_data)
            
            # Motivational messages
            motivational_message = self._generate_streak_motivation(new_streak_data)
            
            streak_update = {
                "current_streak": new_streak_data["current_streak"],
                "longest_streak": new_streak_data["longest_streak"],
                "streak_status": new_streak_data["status"],
                "streak_bonus_xp": self._calculate_streak_bonus_xp(new_streak_data["current_streak"]),
                "personal_records": personal_records,
                "motivational_message": motivational_message,
                "next_milestone": self._get_next_streak_milestone(new_streak_data["current_streak"]),
                "streak_level": self._calculate_streak_level(new_streak_data["current_streak"])
            }
            
            return streak_update
            
        except Exception as e:
            logger.error(f"Streak update failed: {e}")
            return {"current_streak": 1, "error": str(e)}
    
    async def generate_leaderboard(self, leaderboard_type: str = "weekly",
                                 user_id: str = None) -> Dict:
        """
        Gera leaderboard dinâmico
        """
        try:
            logger.info(f"🏅 Generating {leaderboard_type} leaderboard")
            
            # Simular dados do leaderboard
            leaderboard_data = await self._fetch_leaderboard_data(leaderboard_type)
            
            # Ranking personalizado
            user_ranking = await self._get_user_ranking(user_id, leaderboard_data) if user_id else None
            
            # Estatísticas do leaderboard
            leaderboard_stats = self._calculate_leaderboard_stats(leaderboard_data)
            
            # Competições ativas
            active_competitions = await self._get_active_competitions()
            
            leaderboard = {
                "type": leaderboard_type,
                "rankings": leaderboard_data[:50],  # Top 50
                "user_ranking": user_ranking,
                "leaderboard_stats": leaderboard_stats,
                "active_competitions": active_competitions,
                "rewards": self._get_leaderboard_rewards(leaderboard_type),
                "next_update": self._get_next_leaderboard_update(leaderboard_type),
                "motivational_insights": self._generate_leaderboard_insights(
                    user_ranking, leaderboard_stats
                )
            }
            
            return leaderboard
            
        except Exception as e:
            logger.error(f"Leaderboard generation failed: {e}")
            return {"error": str(e)}
    
    async def create_personalized_challenges(self, user_id: str,
                                           user_profile: Dict) -> List[Dict]:
        """
        Cria desafios personalizados para o usuário
        """
        try:
            logger.info(f"🎯 Creating personalized challenges for user: {user_id}")
            
            # Análise do perfil do usuário
            weak_areas = user_profile.get("weak_areas", [])
            learning_style = user_profile.get("learning_style", "mixed")
            current_streak = user_profile.get("current_streak", 0)
            
            challenges = []
            
            # Desafios baseados em áreas fracas
            for area in weak_areas[:2]:
                challenge = {
                    "id": f"improve_{area}_{user_id}",
                    "name": f"Master {area.title()}",
                    "description": f"Improve your {area} skills",
                    "type": "skill_improvement",
                    "target": self._calculate_challenge_target(area, user_profile),
                    "duration": 7,  # dias
                    "rewards": {
                        "xp": 300,
                        "badge": f"{area}_improver"
                    },
                    "progress_tracking": {
                        "current": 0,
                        "required": self._calculate_challenge_target(area, user_profile)
                    }
                }
                challenges.append(challenge)
            
            # Desafio de consistência
            if current_streak < 7:
                challenges.append({
                    "id": f"streak_challenge_{user_id}",
                    "name": "Weekly Consistency",
                    "description": "Study for 7 days in a row",
                    "type": "consistency",
                    "target": 7,
                    "duration": 7,
                    "rewards": {
                        "xp": 500,
                        "badge": "consistency_champion"
                    },
                    "progress_tracking": {
                        "current": current_streak,
                        "required": 7
                    }
                })
            
            # Desafio social
            challenges.append({
                "id": f"social_challenge_{user_id}",
                "name": "Community Learner",
                "description": "Interact with 3 other learners",
                "type": "social",
                "target": 3,
                "duration": 14,
                "rewards": {
                    "xp": 200,
                    "badge": "community_member"
                },
                "progress_tracking": {
                    "current": 0,
                    "required": 3
                }
            })
            
            return challenges
            
        except Exception as e:
            logger.error(f"Challenge creation failed: {e}")
            return []
    
    async def generate_motivation_content(self, user_id: str,
                                        current_performance: Dict) -> Dict:
        """
        Gera conteúdo motivacional personalizado
        """
        try:
            logger.info(f"💪 Generating motivation content for user: {user_id}")
            
            # Análise do estado motivacional
            motivation_state = self._analyze_motivation_state(current_performance)
            
            # Mensagens motivacionais personalizadas
            motivational_messages = self._generate_motivational_messages(motivation_state)
            
            # Conquistas próximas
            upcoming_achievements = await self._get_upcoming_achievements(user_id)
            
            # Progresso visual
            progress_visualization = self._create_progress_visualization(current_performance)
            
            # Dicas de sucesso
            success_tips = self._generate_success_tips(motivation_state)
            
            motivation_content = {
                "motivation_state": motivation_state,
                "primary_message": motivational_messages["primary"],
                "secondary_messages": motivational_messages["secondary"],
                "upcoming_achievements": upcoming_achievements,
                "progress_visualization": progress_visualization,
                "success_tips": success_tips,
                "inspirational_quote": self._get_inspirational_quote(),
                "celebration_data": self._create_motivation_celebration(current_performance),
                "next_milestone": self._get_next_motivation_milestone(current_performance)
            }
            
            return motivation_content
            
        except Exception as e:
            logger.error(f"Motivation content generation failed: {e}")
            return {"error": str(e)}
    
    # Métodos auxiliares
    def _get_base_xp(self, activity_type: str) -> int:
        """Retorna XP base por tipo de atividade"""
        xp_values = {
            "lesson_completion": 50,
            "pronunciation_practice": 30,
            "conversation_practice": 40,
            "grammar_exercise": 25,
            "vocabulary_drill": 20,
            "listening_comprehension": 35,
            "speaking_assessment": 45
        }
        return xp_values.get(activity_type, 20)
    
    def _calculate_performance_multiplier(self, performance_data: Dict) -> float:
        """Calcula multiplicador baseado na performance"""
        score = performance_data.get("score", 50)
        
        if score >= 95:
            return 2.0
        elif score >= 85:
            return 1.5
        elif score >= 70:
            return 1.2
        elif score >= 50:
            return 1.0
        else:
            return 0.8
    
    async def _calculate_consistency_bonus(self, user_id: str) -> int:
        """Calcula bonus de consistência"""
        # Em produção, buscar dados reais de consistência
        consistency_days = 5  # Simular
        
        if consistency_days >= 7:
            return 50
        elif consistency_days >= 3:
            return 25
        else:
            return 0
    
    async def _get_streak_multiplier(self, user_id: str) -> float:
        """Calcula multiplicador de streak"""
        current_streak = 5  # Simular streak atual
        
        if current_streak >= 30:
            return 2.0
        elif current_streak >= 14:
            return 1.5
        elif current_streak >= 7:
            return 1.3
        elif current_streak >= 3:
            return 1.1
        else:
            return 1.0

# Global instance
gamification_engine = GamificationEngine()
