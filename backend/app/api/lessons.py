
# app/api/lessons.py
from fastapi import APIRouter
from app.schemas.lesson import Lesson, AnswerRequest
from app.services.feedback_engine import generate_lesson_feedback

router = APIRouter()

@router.get("/lesson/question", response_model=Lesson)
def get_question():
    return Lesson(
        id=1,
        question_text="Hi, I’m fine ___ you. How are you?",
        options=["thank", "good"],
        correct_option="thank",
        type="question",
        media_url="https://randomuser.me/api/portraits/women/79.jpg"
    )

@router.post("/lesson/answer")
def submit_answer(payload: AnswerRequest):
    feedback = generate_lesson_feedback(payload.user_answer, "thank")
    return feedback
