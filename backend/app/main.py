# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

# Importação futura das rotas por módulo
from app.api import auth, users, lessons, chat, progress, upload

app = FastAPI(
    title="Bilingui-AI Backend",
    description="API para ensino de idiomas com IA, Whisper e gamificação",
    version="1.0.0"
)

# CORS (aceita requisições do mobile)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Substituir por domínio seguro na produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(lessons.router, prefix="/lessons", tags=["Lessons"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(progress.router, prefix="/progress", tags=["Progress"])
app.include_router(upload.router, prefix="/audio", tags=["Audio"])

@app.get("/")
def root():
    return {"message": "🚀 Bilingui-AI Backend is running"}
