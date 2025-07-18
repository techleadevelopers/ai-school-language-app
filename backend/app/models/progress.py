
# app/models/progress.py
from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, String, Text, Boolean, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.base import Base

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    
    # Progresso básico
    percent_complete = Column(Float, default=0.0)
    is_completed = Column(Boolean, default=False)
    
    # Métricas detalhadas
    current_level = Column(String, default="beginner")
    xp_gained = Column(Integer, default=0)
    total_xp = Column(Integer, default=0)
    streak_count = Column(Integer, default=0)
    
    # Performance
    accuracy_score = Column(Float, default=0.0)
    fluency_score = Column(Float, default=0.0)
    pronunciation_score = Column(Float, default=0.0)
    
    # Tempo de estudo
    time_spent_minutes = Column(Integer, default=0)
    session_count = Column(Integer, default=0)
    
    # Dados do curso salvos
    course_data = Column(JSON, default=dict)  # Dados específicos do curso
    learning_objectives = Column(JSON, default=list)  # Objetivos de aprendizado
    strengths = Column(JSON, default=list)  # Pontos fortes
    weaknesses = Column(JSON, default=list)  # Pontos fracos
    
    # Timestamps
    started_at = Column(DateTime, default=datetime.utcnow)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="progress")
    lesson = relationship("Lesson", back_populates="progress")
    
    def update_progress(self, session_data: dict):
        """Atualizar progresso com dados da sessão"""
        self.time_spent_minutes += session_data.get("duration_minutes", 0)
        self.session_count += 1
        self.accuracy_score = session_data.get("accuracy", self.accuracy_score)
        self.fluency_score = session_data.get("fluency", self.fluency_score)
        self.pronunciation_score = session_data.get("pronunciation", self.pronunciation_score)
        self.xp_gained += session_data.get("xp_earned", 0)
        self.total_xp += session_data.get("xp_earned", 0)
        self.last_updated = datetime.utcnow()
        
        # Marcar como completo se atingiu 100%
        if self.percent_complete >= 100.0 and not self.is_completed:
            self.is_completed = True
            self.completed_at = datetime.utcnow()
    
    def save_course_data(self, course_info: dict):
        """Salvar dados específicos do curso"""
        self.course_data = course_info
        self.last_updated = datetime.utcnow()

