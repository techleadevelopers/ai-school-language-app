# app/config.py

import os
from dotenv import load_dotenv
from pydantic import BaseSettings

# Carrega variáveis do arquivo .env (criar depois)
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Bilingui-AI"
    API_VERSION: str = "v1"

    # Banco de dados (ex: SQLite, PostgreSQL)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./bilingui.db")

    # Configurações JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret-key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 dia

    # Caminhos
    UPLOAD_DIR: str = "./static/uploads"
    AUDIO_MODEL_PATH: str = "./models/whisper"
    MISTRAL_MODEL_PATH: str = "./models/mistral"

    # Modo debug
    DEBUG: bool = True

settings = Settings()
