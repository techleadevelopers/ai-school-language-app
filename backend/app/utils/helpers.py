
import os
import re
import logging
from typing import Optional, Dict, List
from fastapi import UploadFile
import mimetypes

logger = logging.getLogger(__name__)

def validate_audio_file(file: UploadFile) -> bool:
    """
    Validate uploaded audio file format and size
    """
    try:
        # Check file extension
        allowed_extensions = {'.wav', '.mp3', '.m4a', '.ogg', '.flac', '.aac'}
        file_extension = os.path.splitext(file.filename)[1].lower()
        
        if file_extension not in allowed_extensions:
            logger.warning(f"Invalid file extension: {file_extension}")
            return False
        
        # Check MIME type
        mime_type, _ = mimetypes.guess_type(file.filename)
        if mime_type and not mime_type.startswith('audio/'):
            logger.warning(f"Invalid MIME type: {mime_type}")
            return False
        
        # Check file size (max 50MB)
        if hasattr(file, 'size') and file.size > 50 * 1024 * 1024:
            logger.warning(f"File too large: {file.size} bytes")
            return False
        
        return True
        
    except Exception as e:
        logger.error(f"File validation failed: {e}")
        return False

def get_current_user(token: str = None) -> Optional[Dict]:
    """
    Get current user from token (placeholder implementation)
    """
    # In production, validate JWT token and return user data
    return {
        "id": "user123",
        "username": "student",
        "level": "intermediate",
        "preferences": {
            "language": "english",
            "difficulty": "intermediate"
        }
    }

def calculate_audio_quality_score(audio_path: str) -> Dict:
    """
    Calculate audio quality metrics
    """
    try:
        # In production, analyze actual audio file
        # For now, return simulated quality metrics
        return {
            "volume_level": "optimal",
            "background_noise": "minimal",
            "clarity_score": 0.92,
            "sample_rate": "44.1kHz",
            "bit_rate": "128kbps",
            "duration": 5.2,
            "quality_rating": "excellent"
        }
        
    except Exception as e:
        logger.error(f"Audio quality calculation failed: {e}")
        return {
            "volume_level": "unknown",
            "background_noise": "unknown",
            "clarity_score": 0.0,
            "quality_rating": "unknown"
        }

def normalize_audio_text(text: str) -> str:
    """
    Normalize audio transcription text for comparison
    """
    try:
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Handle common transcription variations
        text = text.replace("'", "")
        text = text.replace("-", " ")
        
        return text.strip()
        
    except Exception as e:
        logger.error(f"Text normalization failed: {e}")
        return text

def calculate_similarity_score(text1: str, text2: str) -> float:
    """
    Calculate similarity between two texts
    """
    try:
        # Normalize both texts
        norm_text1 = normalize_audio_text(text1)
        norm_text2 = normalize_audio_text(text2)
        
        # Simple word-based similarity
        words1 = set(norm_text1.split())
        words2 = set(norm_text2.split())
        
        if not words1 and not words2:
            return 1.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        similarity = len(intersection) / len(union) if union else 0.0
        return similarity
        
    except Exception as e:
        logger.error(f"Similarity calculation failed: {e}")
        return 0.0

def generate_pronunciation_score(transcription: str, target_text: str, 
                               audio_quality: Dict) -> Dict:
    """
    Generate comprehensive pronunciation score
    """
    try:
        # Calculate base similarity
        similarity = calculate_similarity_score(transcription, target_text)
        
        # Apply audio quality modifier
        quality_modifier = audio_quality.get("clarity_score", 0.8)
        
        # Calculate component scores
        pronunciation_score = similarity * quality_modifier * 100
        fluency_score = min(100, pronunciation_score + (quality_modifier * 10))
        accuracy_score = similarity * 100
        
        return {
            "overall_score": round(pronunciation_score, 1),
            "pronunciation_score": round(pronunciation_score, 1),
            "fluency_score": round(fluency_score, 1),
            "accuracy_score": round(accuracy_score, 1),
            "similarity_score": round(similarity, 3),
            "quality_modifier": round(quality_modifier, 3)
        }
        
    except Exception as e:
        logger.error(f"Pronunciation scoring failed: {e}")
        return {
            "overall_score": 0,
            "pronunciation_score": 0,
            "fluency_score": 0,
            "accuracy_score": 0,
            "similarity_score": 0,
            "quality_modifier": 0
        }

def generate_improvement_suggestions(scores: Dict, transcription: str, 
                                   target_text: str) -> List[str]:
    """
    Generate personalized improvement suggestions
    """
    suggestions = []
    
    try:
        overall_score = scores.get("overall_score", 0)
        
        if overall_score < 50:
            suggestions.extend([
                "Practice speaking more slowly and clearly",
                "Focus on pronouncing each word distinctly",
                "Try breaking down difficult words into syllables",
                "Practice in a quiet environment"
            ])
        elif overall_score < 70:
            suggestions.extend([
                "Work on connecting words smoothly",
                "Practice the rhythm and flow of sentences",
                "Pay attention to stress patterns in words",
                "Record yourself and compare with native speakers"
            ])
        elif overall_score < 85:
            suggestions.extend([
                "Focus on intonation and natural speech patterns",
                "Practice with longer, more complex sentences",
                "Work on reducing pauses between words",
                "Try speaking with more confidence"
            ])
        else:
            suggestions.extend([
                "Excellent pronunciation! Try more challenging content",
                "Practice with native-speed conversations",
                "Focus on advanced pronunciation features",
                "Work on regional accent variations"
            ])
        
        # Add specific suggestions based on transcription analysis
        if transcription.lower() != target_text.lower():
            suggestions.append("Pay attention to word endings and consonant sounds")
        
        return suggestions
        
    except Exception as e:
        logger.error(f"Suggestion generation failed: {e}")
        return ["Keep practicing! Regular practice leads to improvement."]

def format_audio_feedback(analysis_result: Dict) -> Dict:
    """
    Format audio analysis result for frontend consumption
    """
    try:
        formatted = {
            "success": True,
            "scores": {
                "overall": analysis_result.get("overall_score", 0),
                "pronunciation": analysis_result.get("pronunciation_score", 0),
                "fluency": analysis_result.get("fluency_score", 0),
                "accuracy": analysis_result.get("accuracy_score", 0)
            },
            "transcription": analysis_result.get("transcription", ""),
            "feedback": analysis_result.get("feedback", "Keep practicing!"),
            "suggestions": analysis_result.get("improvement_suggestions", []),
            "ai_insights": analysis_result.get("ai_insights", []),
            "next_steps": analysis_result.get("next_steps", []),
            "metadata": {
                "processing_time": analysis_result.get("processing_time", 0),
                "model_confidence": analysis_result.get("model_confidence", 0),
                "audio_quality": analysis_result.get("audio_quality", {})
            }
        }
        
        return formatted
        
    except Exception as e:
        logger.error(f"Feedback formatting failed: {e}")
        return {
            "success": False,
            "error": "Failed to format feedback",
            "scores": {"overall": 0, "pronunciation": 0, "fluency": 0, "accuracy": 0}
        }

def generate_learning_path(user_performance: List[Dict], target_level: str) -> Dict:
    """
    Generate personalized learning path based on performance
    """
    try:
        if not user_performance:
            return {
                "current_level": "beginner",
                "target_level": target_level,
                "recommended_focus": ["basic_pronunciation", "common_phrases"],
                "estimated_duration": "4 weeks"
            }
        
        # Analyze performance trends
        recent_scores = [p.get("score", 0) for p in user_performance[-10:]]
        avg_score = sum(recent_scores) / len(recent_scores) if recent_scores else 0
        
        # Determine current level
        if avg_score >= 85:
            current_level = "advanced"
        elif avg_score >= 70:
            current_level = "intermediate"
        else:
            current_level = "beginner"
        
        # Generate recommendations
        learning_path = {
            "current_level": current_level,
            "target_level": target_level,
            "progress_percentage": min(100, (avg_score / 90) * 100),
            "recommended_focus": _get_focus_areas(current_level, target_level),
            "estimated_duration": _estimate_duration(current_level, target_level),
            "next_milestones": _get_next_milestones(current_level, target_level)
        }
        
        return learning_path
        
    except Exception as e:
        logger.error(f"Learning path generation failed: {e}")
        return {
            "current_level": "beginner",
            "target_level": target_level,
            "error": "Failed to generate learning path"
        }

def _get_focus_areas(current_level: str, target_level: str) -> List[str]:
    """Get focus areas based on current and target levels"""
    focus_map = {
        "beginner": ["basic_pronunciation", "common_phrases", "simple_conversations"],
        "intermediate": ["fluency_building", "complex_sentences", "natural_rhythm"],
        "advanced": ["accent_reduction", "professional_speaking", "cultural_nuances"]
    }
    return focus_map.get(current_level, ["general_practice"])

def _estimate_duration(current_level: str, target_level: str) -> str:
    """Estimate time to reach target level"""
    duration_map = {
        ("beginner", "intermediate"): "6-8 weeks",
        ("beginner", "advanced"): "12-16 weeks",
        ("intermediate", "advanced"): "6-10 weeks"
    }
    return duration_map.get((current_level, target_level), "4-6 weeks")

def _get_next_milestones(current_level: str, target_level: str) -> List[str]:
    """Get next milestones to achieve"""
    milestones = {
        "beginner": ["Achieve 70% pronunciation accuracy", "Complete 20 speaking sessions"],
        "intermediate": ["Maintain 85% fluency score", "Practice advanced conversations"],
        "advanced": ["Perfect accent consistency", "Master professional communication"]
    }
    return milestones.get(current_level, ["Continue regular practice"])
