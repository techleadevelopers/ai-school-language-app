<h1 align="center">🤖 Bilingui-AI</h1>
<p align="center">
  <img src="./assets/images/logo.png" alt="Bilingui-AI Logo" width="160"/>
</p>
<p align="center">
  Aprendizado de idiomas com IA local, gamificação e correção de fala em tempo real.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/IA--Local-Whisper%20%2B%20Mistral-10b2f5?style=flat-square&logo=OpenAI&logoColor=white"/>
  <img src="https://img.shields.io/badge/Mobile-React%20Native-blue?style=flat-square&logo=react"/>
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/UX-Futuristic%20UI%20%2B%20Gamification-facc15?style=flat-square"/>
  <img src="https://img.shields.io/badge/Voice-Whisper%20ASR%20ready-20c997?style=flat-square"/>
</p>

---

## 📚 Índice

- [📌 Visão Geral](#📌-visão-geral)
- [🚀 Funcionalidades](#🚀-funcionalidades)
- [🧠 IA Local](#🧠-ia-local)
- [📱 Mobile App](#📱-mobile-app)
- [⚙️ Backend API](#⚙️-backend-api)
- [🧪 Tecnologias Utilizadas](#🧪-tecnologias-utilizadas)
- [🗂️ Estrutura de Pastas](#🗂️-estrutura-de-pastas)
- [🔧 Como Rodar Localmente](#🔧-como-rodar-localmente)
- [🌐 Roadmap](#🌐-roadmap)
- [🤝 Contribuição](#🤝-contribuição)
- [🧩 Licença](#🧩-licença)

---

## 📌 Visão Geral

**Bilingui-AI** é um app educacional de nova geração que permite o **aprendizado de idiomas com feedback instantâneo**, IA embarcada e gamificação. Ideal para quem quer estudar de forma prática, divertida e sem depender da nuvem para tudo.

🔒 **100% compatível com IA local (offline-ready)**  
🧠 Corrige sua pronúncia e frases em tempo real  
🔥 Sistema de XP, progresso e conquistas  
📚 Geração dinâmica de lições com LLM  
📊 Histórico, exportação, rankings, e muito mais

---

## 🚀 Funcionalidades

| 🔹 Recurso                      | 🧠 Tecnologia          | ✅ Status      |
|-------------------------------|------------------------|----------------|
| Gravação de voz               | `react-native-voice`   | ✅ Implementado |
| Transcrição com Whisper       | `Whisper (local/API)`  | ✅ Integrado    |
| Correções com LLM             | `Mistral 7B / GPT`      | ✅ Operacional  |
| Sistema de XP & Níveis        | `Zustand + LocalStorage`| ✅ Integrado    |
| Lições Dinâmicas              | `LLM + IA adaptativa`  | ✅ Em curso     |
| Exportar histórico em PDF     | `reportlab (backend)`  | 🔜 Em breve     |
| Rankings e conquistas         | `Gamification`         | 🔜 Em curso     |

---

## 🧠 IA Local

| Componente | Modelo | Execução |
|------------|--------|----------|
| Transcrição | Whisper (base/tiny) | `local` via `ffmpeg` + `whisper.cpp` ou `OpenAI API` |
| Correção textual | Mistral-7B (quantizado) | `ollama` local ou backend FastAPI |
| Lições inteligentes | Prompt engineer + LLM | `FastAPI` |

---

## 📱 Mobile App (Expo)

Frontend desenvolvido em **React Native (Expo Router)** com navegação fluida, suporte a dark mode, tipografia customizada e animações otimizadas.

```bash
cd frontend
npm install
npx expo start
Componentes reutilizáveis:

VoiceButton 🎤

XPProgressBar 📈

FeedbackBox ✅

Typography, Container, PrimaryButton

⚙️ Backend API
API desenvolvida em FastAPI com rotas assíncronas e microserviços para:

/transcribe → Transcreve áudio de fala

/llm → Corrige e explica frases

/lesson → Gera lições adaptativas

/progress/:id → Atualiza progresso do usuário

Inicialização rápida
bash
Copiar
Editar
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
🧪 Tecnologias Utilizadas
Frontend
React Native 0.76

Expo Router 4+

Typescript

Zustand

react-native-voice / expo-av

StyledComponents ou NativeWind (opcional)

Paper UI, Blur, SafeArea

Backend
FastAPI

Whisper.cpp / OpenAI Whisper

Mistral 7B com ollama

PostgreSQL + ORM

Celery + Redis (futuro)

DevOps
Docker / Docker Compose

CI/CD com GitHub Actions (em progresso)

Railway / Render / EC2 (opcional)

🗂️ Estrutura de Pastas
bash
Copiar
Editar
bilingui-AI/
├── frontend/
│   ├── app/
│   ├── components/
│   ├── screens/
│   ├── assets/images/
│   ├── service/
│   └── constants/
│
└── backend/
    ├── api/
    ├── services/
    ├── database/
    ├── models/
    └── main.py
🔧 Como Rodar Localmente
Instalar dependências

bash
Copiar
Editar
cd frontend
npm install
Executar app mobile

bash
Copiar
Editar
npx expo start
(Opcional) Rodar backend

bash
Copiar
Editar
cd backend
uvicorn main:app --reload
🌐 Roadmap
 Gravação e transcrição da fala

 Correções com IA

 Sistema de XP e níveis

 Multiplayer em tempo real com WebSocket

 Ranking global com backend Firebase/SQL

 Reconhecimento fonético por idioma

 Testes automatizados E2E com Detox

 Modo criança com avatares e jogos

🤝 Contribuição
Contribuições são muito bem-vindas!
Abra uma issue ou envie um PR com melhorias.

Recomendações:

Nomear commits no padrão convencional

Usar ESLint com npm run lint

