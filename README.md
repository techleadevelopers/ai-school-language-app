<h1 align="center">🤖 Bilingui-AI</h1> <p align="center"> <img src="./frontend/assets/images/logo.png" alt="Bilingui-AI Logo" width="160"/> </p> <p align="center"> Plataforma educacional de idiomas com IA local (Whisper + Mistral), gamificação, chat com IA e feedback de fala em tempo real. </p> <p align="center"> <img src="https://img.shields.io/badge/IA--Local-Whisper%20%2B%20Mistral-10b2f5?style=flat-square&logo=OpenAI&logoColor=white"/> <img src="https://img.shields.io/badge/Mobile-React%20Native-blue?style=flat-square&logo=react"/> <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square&logo=python"/> <img src="https://img.shields.io/badge/UX-Futuristic%20UI%20%2B%20Gamification-facc15?style=flat-square"/> <img src="https://img.shields.io/badge/Voice-Whisper%20ASR%20ready-20c997?style=flat-square"/> </p>

<h1 align="center">🧠 Design UX/UI</h1>
<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1XFdYZy-wOy5CQUmHgW8KtsjjPJThGqQ5" width="740" />
</p>


<h1 align="center">🧠 ROAD SCRUM</h1>
<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1nMTyIStEGwVRQwFnHclYwRlWflhV-dvf" width="740" />
</p>

📚 Índice

📌 Visão Geral

🚀 Funcionalidades

🧠 IA Local

📱 Mobile App (Frontend)

⚙️ Backend API

🧪 Tecnologias Utilizadas

📂 Estrutura de Pastas

🔧 Como Rodar Localmente

🧭 Roadmap SCRUM

🤝 Contribuição

🧉 Licença

📌 Visão Geral

O Bilingui-AI une IA local, UX moderna e aprendizado imersivo de idiomas com:

🎤 Correção de fala por áudio (Whisper)

🧠 Chat com IA contextual (Mistral 7B)

📈 Sistema de progresso e XP

🏆 Gamificação com ranking e conquistas

🗣️ Licao + leitura + fala + perguntas

💬 Feedback em tempo real com IA embarcada

🚀 Funcionalidades

Recurso

Tecnologia

Status

Gravação e transcrição de voz

react-native-voice, Whisper

✅ Pronto

Correção inteligente de frases

Mistral 7B, prompt NLP

✅ Pronto

Sistema de lições adaptativas

FastAPI + IA

✅ Em uso

XP, níveis, medalhas e streaks

Gamificação + Zustand

✅ Em uso

Radar de estatísticas do usuário

FastAPI + Charts frontend

✅ Ativo

Chat IA contextual

Mistral via Ollama

✅ Ativo

PDF de progresso semanal

reportlab (backend)

🔜 Em breve

Multiplayer via sockets

websockets, socket.io

🔜 Em design

🧠 IA Local

🎧 Whisper

Transcrição offline

Correção de pronúncia e fluência

Feedback fonético e sugestão de repetição

🤖 Mistral 7B

Correção de frases e respostas livres

Chat com IA por lição/contexto

Avaliação por similaridade semântica (SentenceTransformer)

📱 Mobile App (Frontend)

Frontend em React Native com Expo Router:

cd frontend
npm install
npx expo start

Componentes integrados:

VoiceButton 🎤

XPProgressBar 📈

FeedbackBox

QuestionScreen.tsx

ProfileScreen com RadarChart

⚙️ Backend API

API em FastAPI, com foco em modularidade, IA, autenticação e gamificação.

Rotas principais:

/auth/login         POST   → Login com JWT
/users/             GET    → Dados do perfil
/lessons/           GET    → Lista de lições
/lesson/question    GET    → Pergunta Q&A
/lesson/answer      POST   → Envia resposta do aluno
/chat/              POST   → Chat com IA
/audio/submit       POST   → Envio de áudio para Whisper
/progress/          GET    → Dados do radar e progresso
/leaderboard/       GET    → Ranking global

🧪 Tecnologias Utilizadas

Frontend

React Native 0.76 + Expo

Expo Router 4.x

Zustand, StyledComponents

react-native-voice, expo-av

Chart.js, Tailwind, NativeWind

Backend

FastAPI + Uvicorn

SQLite (ou PostgreSQL)

SQLAlchemy + Alembic

Whisper.cpp / OpenAI Whisper

Mistral 7B via Ollama

Sentence Transformers

DevOps

Docker + GitHub Actions (CI/CD)

📂 Estrutura de Pastas

bilingui-AI/
├── frontend/
│   ├── app/                  # Screens, layouts
│   ├── components/           # Voice, Progress, Charts
│   ├── assets/images/
│   └── service/              # API calls, Zustand
│
└── backend/
    ├── app/
    │   ├── main.py           # FastAPI entrypoint
    │   ├── models/           # ORM (User, Progress, etc)
    │   ├── schemas/          # Pydantic models
    │   ├── services/         # IA, Whisper, IA Engine
    │   ├── api/              # Rotas modulares
    │   └── utils/            # Helpers, JWT, etc.
    ├── alembic/              # Migrations
    ├── Dockerfile
    ├── requirements.txt
    └── .env

🔧 Como Rodar Localmente

Frontend

cd frontend
npm install
npx expo start

Backend

cd backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn app.main:app --reload

🧭 Roadmap SCRUM

Sprint

Meta

1️⃣

Auth, User, JWT

2️⃣

Lições (reading, speaking, question)

3️⃣

Upload + Transcrição por Whisper

4️⃣

Chat com IA via Mistral

5️⃣

Gamificação + Leaderboard

6️⃣

Estatísticas + RadarChart

7️⃣

Multiplayer + Feedbacks + Refatorações

🤝 Contribuição

Contribuições são bem-vindas!

# Fork o projeto
git checkout -b feature/nova-feature

# Commit com padrão
git commit -m "feat: nova feature x"

# Push para o branch remoto
git push origin feature/nova-feature

# Abra um PR

🧉 Licença

Este projeto está sob a licença MIT — Desenvolvido com 💙 por TechLeadDevelopers
