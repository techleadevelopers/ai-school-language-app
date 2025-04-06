<h1 align="center">🧠 Bilingui-AI Backend</h1>
<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/5068/5068656.png" width="140" />
</p>
<p align="center">
  API avançada para ensino de idiomas com IA Local (Whisper + Mistral), gamificação, chat contextual e correção de fala.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/IA-Whisper%20%7C%20Mistral-20c997?style=flat-square&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/Auth-JWT%20%2B%20OAuth2-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/DevOps-Docker%20%7C%20CI/CD-ffc107?style=flat-square&logo=docker"/>
  <img src="https://img.shields.io/badge/Database-SQLAlchemy%20%7C%20Alembic-4caf50?style=flat-square"/>
</p>

---

## 📚 Índice

- [📌 Visão Geral](#📌-visão-geral)
- [🧪 Tecnologias](#🧪-tecnologias)
- [⚙️ Funcionalidades Backend](#⚙️-funcionalidades-backend)
- [🧠 IA Local](#🧠-ia-local)
- [🗂️ Estrutura de Pastas](#🗂️-estrutura-de-pastas)
- [🔐 Segurança](#🔐-segurança)
- [🧰 Setup Local](#🧰-setup-local)
- [🧪 Testes](#🧪-testes)
- [🚀 DevOps e Deploy](#🚀-devops-e-deploy)
- [🧭 Roadmap SCRUM](#🧭-roadmap-scrum)
- [🤝 Contribuição](#🤝-contribuição)
- [🧩 Licença](#🧩-licença)

---

## 📌 Visão Geral

> API robusta que gerencia:
>
> - 🧑‍🏫 Cursos & lições interativas
> - 🎙️ Áudio do aluno com feedback via **Whisper**
> - 💬 Chat com IA **Mistral 7B local**
> - 📈 Progresso e gamificação
> - 🔐 Login, JWT, roles por tipo de usuário

---

## 🧪 Tecnologias

| Camada           | Ferramentas / Bibliotecas               |
|------------------|------------------------------------------|
| Backend Core     | FastAPI, Uvicorn                        |
| Banco de Dados   | SQLite / PostgreSQL, SQLAlchemy         |
| IA Local         | Whisper.cpp, Mistral via Ollama         |
| Auth             | OAuth2 + JWT                            |
| ORM / Migrations | SQLAlchemy + Alembic                    |
| Áudio & IA       | ffmpeg, PyDub, SentenceTransformers     |
| DevOps           | Docker, GitHub Actions (CI/CD)          |
| Testes           | Pytest, HTTPX, coverage                 |

---

## ⚙️ Funcionalidades Backend

| Rota                      | Método | Descrição                         |
|---------------------------|--------|-----------------------------------|
| `/auth/login`             | POST   | Autenticação JWT                  |
| `/users/`                 | GET    | Retorna dados do perfil           |
| `/lessons/`               | GET    | Lista lições disponíveis          |
| `/lesson/question`        | GET    | Pergunta de Q&A                   |
| `/lesson/answer`          | POST   | Resposta do usuário               |
| `/chat/`                  | POST   | Chat contextual com IA            |
| `/audio/submit`           | POST   | Envia áudio para análise (Whisper)|
| `/progress/`              | GET    | Dados de progresso e radar        |
| `/leaderboard/`           | GET    | Ranking global                    |

---

## 🧠 IA Local

### 🎧 Fala com Whisper

- Upload de áudio (`POST /audio/submit`)
- Transcrição com Whisper Base/Tiny local
- Avaliação fonética + sugestões

### 🤖 Chat com Mistral 7B

- Chat contextual via `POST /chat`
- IA local rodando com [ollama](https://ollama.com)
- Prompts personalizados por lição
- Avaliação por semântica (vector similarity)

---

## 🗂️ Estrutura de Pastas

```bash
bilingui-backend/
│
├── app/
│   ├── main.py              # FastAPI app
│   ├── config.py            # Settings via pydantic
│   ├── models/              # ORM: user, lesson, progress, etc.
│   ├── schemas/             # Pydantic I/O
│   ├── services/            # IA, whisper, chat, ranking
│   ├── api/                 # Rotas modulares
│   └── utils/               # Token, helpers, feedback
│
├── static/                  # Uploads e áudios
├── tests/                   # Pytest
├── alembic/                 # Migrations
├── Dockerfile
└── requirements.txt
🔐 Segurança
JWT assinado com segredo seguro

Expiração configurável (120min)

Roles: admin, student, native

Uploads validados por tipo e extensão

Proteção de endpoints com Depends

🧰 Setup Local
bash
Copiar
Editar
# Crie ambiente
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instale dependências
pip install -r requirements.txt

# Variáveis de ambiente
cp .env.example .env

# Rode a API
uvicorn app.main:app --reload
🧪 Testes
bash
Copiar
Editar
pytest -v
Cobertura para:

Login e auth

Progressão por lição

Upload e transcrição

Chat IA

🚀 DevOps e Deploy
Etapa	Ferramenta
🐳 Docker	Dockerfile pronto
☁️ Deploy	Railway, Fly.io
🔄 CI/CD	GitHub Actions
📊 Logs	Uvicorn + logs stdout
💾 Backups	PostgresDump diário
🧭 Roadmap SCRUM
Sprint	Objetivo
1️⃣	Auth, modelo User, JWT
2️⃣	Lições + Q&A (QuestionScreen)
3️⃣	Upload + Whisper Feedback
4️⃣	Chat com IA via Mistral
5️⃣	Gamificação (XP, streak, leaderboard)
6️⃣	Estatísticas, radar charts, exportações
7️⃣	Refatorações + segurança
🤝 Contribuição
Contribuições são muito bem-vindas! Para colaborar:

Fork o projeto

Crie sua branch (git checkout -b feature/nome)

Faça commit claro (feat: adiciona endpoint x)

Abra PR com descrição

🧩 Licença
Este projeto está sob a licença MIT — sinta-se livre para usar e adaptar!

✨ Desenvolvido com 💙 por TechLeadDevelopers