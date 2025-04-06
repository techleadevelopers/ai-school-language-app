# app/models/lesson.py
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.models.base import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    language = Column(String, index=True)
    level = Column(String, index=True)  # beginner, intermediate, etc.
    title = Column(String)
    type = Column(String)  # reading, listening, speaking, question, chat
    content = Column(Text)

    progress = relationship("Progress", back_populates="lesso