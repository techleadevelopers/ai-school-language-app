# app/services/feedback_engine.py
from typing import Dict


def generate_lesson_feedback(user_answer: str, correct_answer: str) -> Dict:
    correct = user_answer.strip().lower() == correct_answer.strip().lower()
    return {
        "correct": correct,
        "message": "Correct!" if correct else f"Try again. Hint: {correct_answer[:2]}...",
        "score": 100 if correct else 50
    }
