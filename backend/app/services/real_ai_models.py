
import asyncio
import logging
from typing import Dict, List, Optional, Tuple, Any
import numpy as np
from datetime import datetime, timedelta
import json
import re
from dataclasses import dataclass, asdict
from enum import Enum
import torch
import librosa
import soundfile as sf
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import spacy
from sentence_transformers import SentenceTransformer
import whisper
import speech_recognition as sr
from scipy.spatial.distance import cosine
import textstat
from textblob import TextBlob
import requests
import os

logger = logging.getLogger(__name__)

class LanguageLevel(Enum):
    A1 = "beginner"
    A2 = "elementary"
    B1 = "intermediate"
    B2 = "upper_intermediate"
    C1 = "advanced"
    C2 = "proficient"

@dataclass
class RealTimeAnalysis:
    accuracy_score: float
    fluency_score: float
    pronunciation_score: float
    confidence_score: float
    suggestions: List[str]
    detected_errors: List[Dict]
    improvement_areas: List[str]
    next_exercises: List[str]
    estimated_level: LanguageLevel

class RealAIModels:
    """
    Implementação real de modelos de AI para produção
    Focado em resultados reais de aprendizado
    """
    
    def __init__(self):
        self.whisper_model = None
        self.grammar_model = None
        self.sentence_transformer = None
        self.nlp = None
        self.speech_recognizer = None
        self.models_loaded = False
        
    async def initialize_production_models(self):
        """
        Inicializar modelos reais para produção
        """
        try:
            logger.info("🚀 Loading production AI models...")
            
            # Carregar Whisper para transcrição real
            self.whisper_model = whisper.load_model("base")
            logger.info("✅ Whisper model loaded")
            
            # Carregar modelo de gramática
            self.grammar_model = pipeline(
                "text-classification",
                model="textattack/roberta-base-CoLA",
                return_all_scores=True
            )
            logger.info("✅ Grammar model loaded")
            
            # Carregar sentence transformer para análise semântica
            self.sentence_transformer = SentenceTransformer('all-MiniLM-L6-v2')
            logger.info("✅ Sentence transformer loaded")
            
            # Carregar spaCy para análise linguística
            try:
                self.nlp = spacy.load("en_core_web_sm")
            except OSError:
                logger.warning("⚠️ spaCy model not found, using basic NLP")
                self.nlp = None
            
            # Inicializar reconhecedor de fala
            self.speech_recognizer = sr.Recognizer()
            
            self.models_loaded = True
            logger.info("✅ All production AI models loaded successfully")
            
        except Exception as e:
            logger.error(f"❌ Failed to load production models: {e}")
            raise

    async def analyze_speech_real(self, audio_file_path: str, target_text: str, 
                                 user_level: str) -> RealTimeAnalysis:
        """
        Análise real de fala com múltiplos modelos
        """
        try:
            if not self.models_loaded:
                await self.initialize_production_models()
            
            # Carregar áudio
            audio, sr_rate = librosa.load(audio_file_path, sr=16000)
            
            # Transcrição com Whisper
            result = self.whisper_model.transcribe(audio_file_path)
            transcription = result["text"].strip()
            
            # Análise de precisão
            accuracy = self._calculate_accuracy(transcription, target_text)
            
            # Análise de fluência
            fluency = self._analyze_fluency(audio, sr_rate)
            
            # Análise de pronúncia
            pronunciation = self._analyze_pronunciation(transcription, target_text)
            
            # Análise de confiança
            confidence = result.get("confidence", 0.8)
            
            # Detectar erros específicos
            errors = self._detect_speech_errors(transcription, target_text)
            
            # Gerar sugestões
            suggestions = self._generate_speech_suggestions(errors, user_level)
            
            # Áreas de melhoria
            improvement_areas = self._identify_improvement_areas(errors, accuracy, fluency)
            
            # Próximos exercícios
            next_exercises = self._recommend_next_exercises(improvement_areas, user_level)
            
            # Estimar nível
            estimated_level = self._estimate_language_level(accuracy, fluency, pronunciation)
            
            return RealTimeAnalysis(
                accuracy_score=accuracy,
                fluency_score=fluency,
                pronunciation_score=pronunciation,
                confidence_score=confidence,
                suggestions=suggestions,
                detected_errors=errors,
                improvement_areas=improvement_areas,
                next_exercises=next_exercises,
                estimated_level=estimated_level
            )
            
        except Exception as e:
            logger.error(f"Speech analysis failed: {e}")
            raise

    async def analyze_text_comprehension(self, user_text: str, reference_text: str) -> Dict:
        """
        Análise real de compreensão textual
        """
        try:
            # Análise de similaridade semântica
            user_embedding = self.sentence_transformer.encode([user_text])
            reference_embedding = self.sentence_transformer.encode([reference_text])
            
            similarity = 1 - cosine(user_embedding[0], reference_embedding[0])
            
            # Análise gramatical
            grammar_analysis = self.grammar_model(user_text)
            grammar_score = max([score['score'] for score in grammar_analysis[0] 
                               if score['label'] == 'ACCEPTABLE'])
            
            # Análise de complexidade
            complexity = self._analyze_text_complexity(user_text)
            
            # Análise de vocabulário
            vocabulary_analysis = self._analyze_vocabulary(user_text)
            
            return {
                "semantic_similarity": similarity,
                "grammar_score": grammar_score,
                "complexity_level": complexity,
                "vocabulary_analysis": vocabulary_analysis,
                "overall_comprehension": (similarity + grammar_score) / 2,
                "feedback": self._generate_text_feedback(similarity, grammar_score, complexity)
            }
            
        except Exception as e:
            logger.error(f"Text comprehension analysis failed: {e}")
            raise

    async def generate_personalized_content(self, user_profile: Dict, 
                                          learning_history: List[Dict]) -> Dict:
        """
        Geração real de conteúdo personalizado baseado em AI
        """
        try:
            # Analisar padrões de aprendizado
            learning_patterns = self._analyze_learning_patterns(learning_history)
            
            # Identificar lacunas de conhecimento
            knowledge_gaps = self._identify_knowledge_gaps(learning_history)
            
            # Gerar exercícios adaptativos
            adaptive_exercises = self._generate_adaptive_exercises(
                user_profile, knowledge_gaps, learning_patterns
            )
            
            # Criar desafios personalizados
            personalized_challenges = self._create_personalized_challenges(
                user_profile, learning_patterns
            )
            
            return {
                "learning_patterns": learning_patterns,
                "knowledge_gaps": knowledge_gaps,
                "adaptive_exercises": adaptive_exercises,
                "personalized_challenges": personalized_challenges,
                "recommended_focus": self._recommend_focus_areas(knowledge_gaps),
                "estimated_progress_time": self._estimate_progress_time(
                    user_profile, learning_patterns
                )
            }
            
        except Exception as e:
            logger.error(f"Personalized content generation failed: {e}")
            raise

    def _calculate_accuracy(self, transcription: str, target: str) -> float:
        """Calcular precisão real da transcrição"""
        words_transcribed = set(transcription.lower().split())
        words_target = set(target.lower().split())
        
        if not words_target:
            return 0.0
            
        correct_words = words_transcribed.intersection(words_target)
        return len(correct_words) / len(words_target)

    def _analyze_fluency(self, audio: np.ndarray, sr: int) -> float:
        """Analisar fluência real baseada em características do áudio"""
        # Detectar pausas
        rms = librosa.feature.rms(y=audio)[0]
        pause_threshold = np.mean(rms) * 0.1
        pauses = np.where(rms < pause_threshold)[0]
        
        # Calcular taxa de fala
        duration = len(audio) / sr
        speech_rate = len(audio) / duration if duration > 0 else 0
        
        # Análise de ritmo
        tempo = librosa.beat.tempo(y=audio, sr=sr)
        
        # Score de fluência baseado em múltiplos fatores
        pause_penalty = len(pauses) / len(rms)
        fluency_score = max(0, 1 - pause_penalty) * min(1, speech_rate / 1000)
        
        return float(fluency_score)

    def _analyze_pronunciation(self, transcription: str, target: str) -> float:
        """Analisar pronúncia comparando transcrição com target"""
        # Análise fonética simples
        transcription_clean = re.sub(r'[^\w\s]', '', transcription.lower())
        target_clean = re.sub(r'[^\w\s]', '', target.lower())
        
        # Calcular distância de Levenshtein
        def levenshtein_distance(s1, s2):
            if len(s1) < len(s2):
                return levenshtein_distance(s2, s1)
            
            if len(s2) == 0:
                return len(s1)
            
            previous_row = range(len(s2) + 1)
            for i, c1 in enumerate(s1):
                current_row = [i + 1]
                for j, c2 in enumerate(s2):
                    insertions = previous_row[j + 1] + 1
                    deletions = current_row[j] + 1
                    substitutions = previous_row[j] + (c1 != c2)
                    current_row.append(min(insertions, deletions, substitutions))
                previous_row = current_row
            
            return previous_row[-1]
        
        distance = levenshtein_distance(transcription_clean, target_clean)
        max_length = max(len(transcription_clean), len(target_clean))
        
        return 1 - (distance / max_length) if max_length > 0 else 0

    def _detect_speech_errors(self, transcription: str, target: str) -> List[Dict]:
        """Detectar erros específicos na fala"""
        errors = []
        
        # Erros de palavras omitidas
        transcription_words = set(transcription.lower().split())
        target_words = set(target.lower().split())
        
        missing_words = target_words - transcription_words
        extra_words = transcription_words - target_words
        
        for word in missing_words:
            errors.append({
                "type": "missing_word",
                "word": word,
                "suggestion": f"Include the word '{word}'"
            })
        
        for word in extra_words:
            errors.append({
                "type": "extra_word",
                "word": word,
                "suggestion": f"Remove the word '{word}'"
            })
        
        return errors

    def _generate_speech_suggestions(self, errors: List[Dict], user_level: str) -> List[str]:
        """Gerar sugestões específicas para melhoria"""
        suggestions = []
        
        if not errors:
            suggestions.append("Great job! Your pronunciation is very clear.")
            return suggestions
        
        error_types = [error["type"] for error in errors]
        
        if "missing_word" in error_types:
            suggestions.append("Try to speak more slowly and include all words.")
        
        if "extra_word" in error_types:
            suggestions.append("Focus on the exact phrase and avoid adding extra words.")
        
        if user_level in ["beginner", "elementary"]:
            suggestions.append("Practice repeating the phrase several times.")
        else:
            suggestions.append("Work on connecting words more naturally.")
        
        return suggestions

    def _identify_improvement_areas(self, errors: List[Dict], accuracy: float, 
                                  fluency: float) -> List[str]:
        """Identificar áreas específicas para melhoria"""
        areas = []
        
        if accuracy < 0.7:
            areas.append("pronunciation_accuracy")
        
        if fluency < 0.6:
            areas.append("speech_fluency")
        
        if len(errors) > 3:
            areas.append("word_clarity")
        
        return areas

    def _recommend_next_exercises(self, improvement_areas: List[str], 
                                 user_level: str) -> List[str]:
        """Recomendar próximos exercícios baseado na análise"""
        exercises = []
        
        if "pronunciation_accuracy" in improvement_areas:
            exercises.append("phonetic_drills")
            exercises.append("minimal_pairs_practice")
        
        if "speech_fluency" in improvement_areas:
            exercises.append("rhythm_practice")
            exercises.append("connected_speech")
        
        if "word_clarity" in improvement_areas:
            exercises.append("word_stress_practice")
            exercises.append("articulation_exercises")
        
        return exercises

    def _estimate_language_level(self, accuracy: float, fluency: float, 
                               pronunciation: float) -> LanguageLevel:
        """Estimar nível de idioma baseado nas métricas"""
        overall_score = (accuracy + fluency + pronunciation) / 3
        
        if overall_score >= 0.9:
            return LanguageLevel.C2
        elif overall_score >= 0.8:
            return LanguageLevel.C1
        elif overall_score >= 0.7:
            return LanguageLevel.B2
        elif overall_score >= 0.6:
            return LanguageLevel.B1
        elif overall_score >= 0.5:
            return LanguageLevel.A2
        else:
            return LanguageLevel.A1

    def _analyze_text_complexity(self, text: str) -> Dict:
        """Analisar complexidade do texto"""
        return {
            "flesch_reading_ease": textstat.flesch_reading_ease(text),
            "flesch_kincaid_grade": textstat.flesch_kincaid_grade(text),
            "sentence_count": textstat.sentence_count(text),
            "word_count": textstat.lexicon_count(text),
            "difficulty_level": textstat.reading_difficulty(text)
        }

    def _analyze_vocabulary(self, text: str) -> Dict:
        """Analisar vocabulário usado"""
        blob = TextBlob(text)
        words = blob.words
        
        return {
            "word_count": len(words),
            "unique_words": len(set(words)),
            "average_word_length": np.mean([len(word) for word in words]),
            "vocabulary_diversity": len(set(words)) / len(words) if words else 0,
            "sentiment": blob.sentiment.polarity
        }

    def _generate_text_feedback(self, similarity: float, grammar_score: float, 
                              complexity: Dict) -> List[str]:
        """Gerar feedback específico para texto"""
        feedback = []
        
        if similarity >= 0.8:
            feedback.append("Excellent understanding of the content!")
        elif similarity >= 0.6:
            feedback.append("Good comprehension, but could be more precise.")
        else:
            feedback.append("Try to focus more on the main ideas.")
        
        if grammar_score >= 0.8:
            feedback.append("Great grammar usage!")
        elif grammar_score >= 0.6:
            feedback.append("Good grammar, with minor issues.")
        else:
            feedback.append("Focus on improving grammar structure.")
        
        return feedback

    def _analyze_learning_patterns(self, history: List[Dict]) -> Dict:
        """Analisar padrões reais de aprendizado"""
        if not history:
            return {"pattern": "new_learner", "consistency": 0.0}
        
        # Analisar consistência
        dates = [datetime.fromisoformat(item.get("date", datetime.now().isoformat())) 
                for item in history]
        consistency = self._calculate_consistency(dates)
        
        # Analisar progresso
        scores = [item.get("score", 0) for item in history]
        progress_trend = self._calculate_trend(scores)
        
        return {
            "consistency_score": consistency,
            "progress_trend": progress_trend,
            "learning_velocity": self._calculate_learning_velocity(history),
            "preferred_time": self._identify_preferred_time(history),
            "strong_areas": self._identify_strong_areas(history),
            "weak_areas": self._identify_weak_areas(history)
        }

    def _calculate_consistency(self, dates: List[datetime]) -> float:
        """Calcular consistência de estudo"""
        if len(dates) < 2:
            return 0.0
        
        dates_sorted = sorted(dates)
        gaps = [(dates_sorted[i+1] - dates_sorted[i]).days 
               for i in range(len(dates_sorted)-1)]
        
        ideal_gap = 1  # 1 dia
        consistency = 1 - (np.mean(gaps) / ideal_gap) if gaps else 0
        
        return max(0.0, min(1.0, consistency))

    def _calculate_trend(self, scores: List[float]) -> str:
        """Calcular tendência de progresso"""
        if len(scores) < 2:
            return "insufficient_data"
        
        # Regressão linear simples
        x = np.arange(len(scores))
        slope = np.polyfit(x, scores, 1)[0]
        
        if slope > 0.1:
            return "improving"
        elif slope < -0.1:
            return "declining"
        else:
            return "stable"

    def _calculate_learning_velocity(self, history: List[Dict]) -> float:
        """Calcular velocidade de aprendizado"""
        if len(history) < 2:
            return 0.0
        
        scores = [item.get("score", 0) for item in history]
        time_span = len(history)
        
        velocity = (scores[-1] - scores[0]) / time_span if time_span > 0 else 0
        return max(0.0, velocity)

    def _identify_preferred_time(self, history: List[Dict]) -> str:
        """Identificar horário preferido de estudo"""
        times = [datetime.fromisoformat(item.get("date", datetime.now().isoformat())).hour 
                for item in history]
        
        if not times:
            return "unknown"
        
        # Encontrar horário mais comum
        from collections import Counter
        most_common_hour = Counter(times).most_common(1)[0][0]
        
        if 6 <= most_common_hour < 12:
            return "morning"
        elif 12 <= most_common_hour < 18:
            return "afternoon"
        else:
            return "evening"

    def _identify_strong_areas(self, history: List[Dict]) -> List[str]:
        """Identificar áreas fortes do usuário"""
        areas = {}
        for item in history:
            skill = item.get("skill", "general")
            score = item.get("score", 0)
            
            if skill not in areas:
                areas[skill] = []
            areas[skill].append(score)
        
        strong_areas = []
        for skill, scores in areas.items():
            if np.mean(scores) >= 0.8:
                strong_areas.append(skill)
        
        return strong_areas

    def _identify_weak_areas(self, history: List[Dict]) -> List[str]:
        """Identificar áreas fracas do usuário"""
        areas = {}
        for item in history:
            skill = item.get("skill", "general")
            score = item.get("score", 0)
            
            if skill not in areas:
                areas[skill] = []
            areas[skill].append(score)
        
        weak_areas = []
        for skill, scores in areas.items():
            if np.mean(scores) < 0.6:
                weak_areas.append(skill)
        
        return weak_areas

    def _identify_knowledge_gaps(self, history: List[Dict]) -> List[str]:
        """Identificar lacunas de conhecimento"""
        gaps = []
        
        # Analisar padrões de erros
        error_patterns = {}
        for item in history:
            errors = item.get("errors", [])
            for error in errors:
                error_type = error.get("type", "unknown")
                if error_type not in error_patterns:
                    error_patterns[error_type] = 0
                error_patterns[error_type] += 1
        
        # Identificar gaps baseado em erros recorrentes
        for error_type, count in error_patterns.items():
            if count >= 3:  # Erro recorrente
                gaps.append(error_type)
        
        return gaps

    def _generate_adaptive_exercises(self, profile: Dict, gaps: List[str], 
                                   patterns: Dict) -> List[Dict]:
        """Gerar exercícios adaptativos baseados em IA"""
        exercises = []
        
        user_level = profile.get("level", "beginner")
        learning_style = profile.get("learning_style", "visual")
        
        for gap in gaps:
            if gap == "pronunciation_accuracy":
                exercises.append({
                    "type": "pronunciation_drill",
                    "difficulty": user_level,
                    "style": learning_style,
                    "content": self._generate_pronunciation_exercise(user_level),
                    "estimated_time": 5
                })
            
            elif gap == "grammar":
                exercises.append({
                    "type": "grammar_practice",
                    "difficulty": user_level,
                    "style": learning_style,
                    "content": self._generate_grammar_exercise(user_level),
                    "estimated_time": 10
                })
            
            elif gap == "vocabulary":
                exercises.append({
                    "type": "vocabulary_builder",
                    "difficulty": user_level,
                    "style": learning_style,
                    "content": self._generate_vocabulary_exercise(user_level),
                    "estimated_time": 8
                })
        
        return exercises

    def _generate_pronunciation_exercise(self, level: str) -> Dict:
        """Gerar exercício de pronúncia específico"""
        exercises_by_level = {
            "beginner": {
                "phrases": ["Hello, how are you?", "Nice to meet you", "Thank you very much"],
                "focus": "basic_sounds",
                "tips": "Focus on clear vowel sounds"
            },
            "intermediate": {
                "phrases": ["I'd like to make a reservation", "Could you please help me?", "What time does it start?"],
                "focus": "connected_speech",
                "tips": "Practice linking words together"
            },
            "advanced": {
                "phrases": ["I couldn't have imagined", "The weather's been unpredictable", "It's a pleasure to meet you"],
                "focus": "complex_sounds",
                "tips": "Work on stress patterns and intonation"
            }
        }
        
        return exercises_by_level.get(level, exercises_by_level["beginner"])

    def _generate_grammar_exercise(self, level: str) -> Dict:
        """Gerar exercício de gramática específico"""
        exercises_by_level = {
            "beginner": {
                "type": "fill_in_blank",
                "sentence": "She ___ (go) to school every day.",
                "correct_answer": "goes",
                "explanation": "Use 'goes' for third person singular in present simple"
            },
            "intermediate": {
                "type": "sentence_transformation",
                "original": "I have never been to Paris.",
                "instruction": "Change to question form",
                "correct_answer": "Have you ever been to Paris?"
            },
            "advanced": {
                "type": "error_correction",
                "sentence": "If I would have more time, I would travel more.",
                "correct_answer": "If I had more time, I would travel more.",
                "explanation": "Use 'had' not 'would have' in the if-clause"
            }
        }
        
        return exercises_by_level.get(level, exercises_by_level["beginner"])

    def _generate_vocabulary_exercise(self, level: str) -> Dict:
        """Gerar exercício de vocabulário específico"""
        exercises_by_level = {
            "beginner": {
                "type": "word_matching",
                "words": ["cat", "dog", "bird", "fish"],
                "definitions": ["pet that meows", "pet that barks", "animal that flies", "animal that swims"],
                "context": "Animals and pets"
            },
            "intermediate": {
                "type": "synonym_practice",
                "word": "happy",
                "synonyms": ["joyful", "cheerful", "content", "pleased"],
                "sentence": "She was very ___ about her promotion."
            },
            "advanced": {
                "type": "contextual_usage",
                "word": "meticulous",
                "definition": "showing great attention to detail; very careful",
                "examples": ["He was meticulous in his research", "The meticulous planning paid off"]
            }
        }
        
        return exercises_by_level.get(level, exercises_by_level["beginner"])

    def _create_personalized_challenges(self, profile: Dict, patterns: Dict) -> List[Dict]:
        """Criar desafios personalizados"""
        challenges = []
        
        consistency = patterns.get("consistency_score", 0.0)
        
        if consistency < 0.5:
            challenges.append({
                "type": "consistency_challenge",
                "title": "7-Day Study Streak",
                "description": "Study for 7 consecutive days",
                "reward": "Consistency Master Badge",
                "difficulty": "medium"
            })
        
        if patterns.get("progress_trend") == "declining":
            challenges.append({
                "type": "improvement_challenge",
                "title": "Score Improvement",
                "description": "Improve your average score by 10%",
                "reward": "Comeback Champion Badge",
                "difficulty": "hard"
            })
        
        return challenges

    def _recommend_focus_areas(self, gaps: List[str]) -> List[str]:
        """Recomendar áreas de foco baseado em gaps"""
        focus_areas = []
        
        if "pronunciation_accuracy" in gaps:
            focus_areas.append("Daily pronunciation practice")
        
        if "grammar" in gaps:
            focus_areas.append("Grammar structure review")
        
        if "vocabulary" in gaps:
            focus_areas.append("Vocabulary expansion exercises")
        
        return focus_areas

    def _estimate_progress_time(self, profile: Dict, patterns: Dict) -> Dict:
        """Estimar tempo de progresso baseado em dados reais"""
        current_level = profile.get("level", "beginner")
        learning_velocity = patterns.get("learning_velocity", 0.1)
        consistency = patterns.get("consistency_score", 0.5)
        
        # Calcular tempo estimado baseado em múltiplos fatores
        base_time = {
            "beginner": 180,  # dias
            "intermediate": 120,
            "advanced": 90
        }
        
        time_estimate = base_time.get(current_level, 180)
        
        # Ajustar baseado na velocidade de aprendizado
        if learning_velocity > 0.2:
            time_estimate *= 0.8
        elif learning_velocity < 0.1:
            time_estimate *= 1.2
        
        # Ajustar baseado na consistência
        time_estimate *= (2 - consistency)
        
        return {
            "next_level_days": int(time_estimate),
            "fluency_months": int(time_estimate * 3 / 30),
            "confidence_level": 0.85 if consistency > 0.7 else 0.65
        }

# Instância global
real_ai_models = RealAIModels()
