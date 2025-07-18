Documentação do Projeto Bilingui-AI
1. Visão Geral do Projeto
O Bilingui-AI é uma plataforma educacional de idiomas inovadora que une inteligência artificial local, um design de experiência do usuário (UX) moderno e uma abordagem de aprendizado imersiva. Seu objetivo principal é fornecer feedback de fala em tempo real, correção inteligente de frases e um ambiente gamificado para tornar o aprendizado de idiomas mais eficaz e envolvente.

Principais Características:

Correção de Fala por Áudio: Utiliza IA para transcrever e analisar a fala do usuário, oferecendo feedback detalhado sobre pronúncia e fluência.
Chat com IA Contextual: Permite conversas interativas com uma IA que se adapta ao contexto da lição ou do usuário.
Sistema de Progresso e XP: Gamifica o aprendizado com pontos de experiência (XP), níveis, medalhas e sequências de estudo (streaks).
Lições Adaptativas: Oferece diferentes tipos de lições (leitura, escuta, fala, perguntas e respostas) que podem se adaptar ao nível do aluno.
Feedback em Tempo Real: Fornece feedback imediato sobre respostas e pronúncia.
2. Arquitetura do Sistema
O Bilingui-AI adota uma arquitetura de cliente-servidor, com um aplicativo móvel (frontend) e uma API de backend que gerencia a lógica de negócios, a persistência de dados e a integração com os modelos de IA.

gherkin

Copiar
+-------------------+       +---------------------+       +-------------------+       +-----------------+
|   Mobile App      |       |      Backend API    |       |  Modelos de IA    |       |   Banco de Dados  |
|   (React Native)  |       |   (FastAPI/Python)  |       | (Whisper, Mistral)|       |   (SQLAlchemy)    |
+-------------------+       +---------------------+       +-------------------+       +-----------------+
|                   |       |                     |       |                   |       |                 |
| - Telas de Lições |       | - Autenticação JWT  |       | - Transcrição     |       | - Usuários      |
| - Prática de Fala |       | - Gerenciamento Usu.  |------>| - Geração de Texto|------>| - Progresso     |
| - Chat com IA     |       | - Lições e Progresso|       | - Análise de Fala |       | - Lições        |
| - Perfil/Ranking  |       | - Chat com IA       |       |                   |       | - Logs de Chat  |
|                   |       | - Upload de Áudio   |       |                   |       | - Submissões Áudio|
+-------------------+       +---------------------+       +-------------------+       +-----------------+
2.1. Fluxo de Dados Exemplo (Prática de Fala):
Usuário Grava Áudio: No aplicativo móvel (tela "Explorar"), o usuário pressiona o botão de microfone e fala uma frase.
Upload de Áudio: O áudio gravado é enviado para o endpoint /audio/submit na API de Backend.
Processamento Whisper: A API recebe o arquivo de áudio e o encaminha para o serviço Whisper (local ou via API) para transcrição e avaliação.
Feedback de Fala: O serviço Whisper retorna a transcrição, uma pontuação e feedback sobre a pronúncia.
Persistência e Resposta: A API armazena a submissão de áudio e o feedback no banco de dados e envia a resposta de volta para o aplicativo móvel.
Exibição de Feedback: O aplicativo móvel exibe o feedback ao usuário, incluindo a correção da frase e sugestões de melhoria.
3. Funcionalidades Detalhadas
Recurso	Tecnologia	Status	Descrição
Gravação e Transcrição de Voz	react-native-voice, Whisper	✅ Pronto	Permite ao usuário gravar sua fala e a IA transcreve o áudio em texto.
Correção Inteligente de Frases	Mistral 7B, prompt NLP	✅ Pronto	Analisa a frase falada ou digitada pelo usuário e oferece correções gramaticais e de uso.
Sistema de Lições Adaptativas	FastAPI + IA	✅ Em uso	Oferece lições em diferentes formatos (leitura, fala, perguntas, chat) que podem ser adaptadas ao nível e idioma do aluno.
XP, Níveis, Medalhas e Streaks	Gamificação + Zustand (Frontend)	✅ Em uso	Implementa um sistema de pontos de experiência, níveis e conquistas para motivar o aprendizado.
Radar de Estatísticas do Usuário	FastAPI + Charts frontend	✅ Ativo	Visualiza o progresso do usuário em diferentes habilidades ou idiomas através de um gráfico radar.
Chat IA Contextual	Mistral via Ollama	✅ Ativo	Permite conversas livres com a IA, que mantém o contexto da lição ou do histórico de chat.
PDF de Progresso Semanal	reportlab (backend)	🔜 Em breve	Geração de relatórios semanais de progresso em formato PDF.
Multiplayer via Sockets	websockets, socket.io	🔜 Em design	Funcionalidade futura para interação entre usuários em tempo real.
4. Tecnologias Utilizadas
4.1. Frontend (Mobile App)
React Native 0.76 + Expo: Framework para construção de aplicativos móveis multiplataforma.
Expo Router 4.x: Solução de roteamento baseada em arquivos para aplicativos Expo.
Zustand: Uma pequena e rápida biblioteca de gerenciamento de estado.
react-native-voice: Para funcionalidades de reconhecimento de fala e gravação de áudio.
expo-av: Módulo Expo para reprodução e gravação de áudio/vídeo.
@expo/vector-icons: Biblioteca de ícones.
react-native-safe-area-context: Para lidar com áreas seguras em dispositivos móveis.
@react-navigation/native: Para temas e navegação.
Chart.js: Para visualização de dados (mencionado no README, mas não diretamente visível nos arquivos .tsx fornecidos, que usam componentes de UI nativos).
Tailwind, NativeWind: Para estilização (mencionado no README, mas os arquivos .tsx usam StyleSheet.create e cores diretas ou de Colors.ts).
4.2. Backend (API)
FastAPI: Framework web Python moderno e rápido para construção de APIs.
Uvicorn: Servidor ASGI para rodar aplicações FastAPI.
SQLAlchemy: ORM (Object Relational Mapper) para interação com o banco de dados.
Alembic: Ferramenta de migração de banco de dados para SQLAlchemy.
SQLite (ou PostgreSQL): Banco de dados padrão (SQLite) ou configurável (PostgreSQL).
python-jose: Para manipulação de tokens JWT.
python-dotenv: Para carregar variáveis de ambiente.
pydantic: Para validação de dados e serialização/desserialização de schemas.
4.3. IA Local
Whisper.cpp / OpenAI Whisper:
Função: Transcrição de áudio para texto.
Uso: Correção de pronúncia e fluência, feedback fonético e sugestão de repetição.
Detalhes: Permite transcrição offline, crucial para feedback em tempo real e privacidade.
Mistral 7B:
Função: Geração de texto e compreensão de linguagem natural.
Uso: Correção de frases e respostas livres, chat contextual com IA.
Detalhes: Acesso via Ollama (mencionado no README), o que implica que o modelo pode ser executado localmente.
Sentence Transformers:
Função: Avaliação por similaridade semântica (mencionado no README).
Uso: Comparar o significado de frases para feedback mais inteligente.
5. Estrutura de Pastas
awk

Copiar
bilingui-AI/
├── frontend/
│   ├── app/                  # Telas e layouts do Expo Router
│   │   ├── (tabs)/           # Layout e telas principais (index, explore)
│   │   ├── _layout.tsx       # Layout global (autenticação, tema)
│   │   ├── +not-found.tsx    # Tela 404
│   │   └── login.tsx         # Tela de Login
│   ├── assets/images/        # Imagens estáticas (logo.png)
│   ├── components/           # Componentes UI reutilizáveis (ParallaxScrollView, Typography, etc.)
│   ├── constants/            # Constantes (Colors.ts)
│   ├── hooks/                # Hooks personalizados (useColorScheme, useThemeColor)
│   ├── screens/              # Telas que não são parte das abas (LessonScreen, ProgressScreen)
│   ├── service/              # Chamadas de API (api.ts)
│   └── ... (outros arquivos de configuração do Expo)
│
└── backend/
    ├── app/
    │   ├── main.py           # Ponto de entrada da aplicação FastAPI
    │   ├── api/              # Rotas da API (auth, users, lessons, chat, progress, upload)
    │   ├── models/           # Modelos ORM do SQLAlchemy (user, progress, lesson, chat_log, audio_submission, base)
    │   ├── schemas/          # Modelos Pydantic para validação de dados (auth, user, lesson, chat_log, progress, response)
    │   ├── services/         # Lógica de negócio e integrações de IA (feedback_engine, mistral_service, whisper_service, leaderboard)
    │   └── utils/            # Utilitários (token, helpers)
    ├── alembic/              # Arquivos de migração do banco de dados
    ├── Dockerfile            # Configuração para Docker
    ├── requirements.txt      # Dependências Python
    └── .env                  # Variáveis de ambiente
6. API Endpoints (Backend - FastAPI)
A API é construída com FastAPI, oferecendo endpoints modulares para diferentes funcionalidades.

6.1. Autenticação (app/api/auth.py)
POST /auth/login
Descrição: Autentica um usuário com email e senha.
Request Body: LoginRequest (email, password)
Response: LoginResponse (access_token, token_type)
Erros: 401 Unauthorized (Invalid credentials)
6.2. Usuários (app/api/users.py)
GET /users/profile
Descrição: Retorna o perfil do usuário autenticado.
Response: UserProfile (id, name, email, role, avatar_url, language_progress)
6.3. Lições (app/api/lessons.py)
GET /lessons/question
Descrição: Retorna uma questão de lição para o usuário.
Response: Lesson (id, question_text, options, correct_option, type, media_url)
POST /lessons/answer
Descrição: Submete a resposta do usuário a uma questão e retorna feedback.
Request Body: AnswerRequest (user_answer)
Response: Objeto JSON com correct (bool), message (str) e score (int).
6.4. Chat (app/api/chat.py)
POST /chat
Descrição: Envia mensagens para o modelo de chat IA (Mistral) e recebe uma resposta contextual.
Request Body: ChatRequest (messages, context)
Response: Objeto JSON com response (str).
6.5. Progresso (app/api/progress.py)
GET /users/progress
Descrição: Retorna o progresso de aprendizado do usuário.
Response: Objeto JSON (simulado) com dados de progresso.
6.6. Áudio (app/api/upload.py)
POST /audio/submit
Descrição: Recebe um arquivo de áudio do usuário para processamento via Whisper.
Request Body: UploadFile (o arquivo de áudio)
Response: Objeto JSON com transcription (str), score (int) e feedback (str).
7. Modelos de Banco de Dados (SQLAlchemy ORM)
Os modelos ORM são definidos em app/models/.

User (app/models/user.py)
Tabela: users
Campos: id, email, hashed_password, name, avatar_url, role, created_at.
Relacionamentos: progress, audio_submissions, chat_logs.
Progress (app/models/progress.py)
Tabela: progress
Campos: id, user_id (FK para users), lesson_id (FK para lessons), percent_complete, last_updated.
Relacionamentos: user, lesson.
Lesson (app/models/lesson.py)
Tabela: lessons
Campos: id, language, level, title, type, content.
Relacionamentos: progress.
ChatLog (app/models/chat_log.py)
Tabela: chat_logs
Campos: id, user_id (FK para users), message, response, timestamp.
Relacionamentos: user.
AudioSubmission (app/models/audio_submission.py)
Tabela: audio_submissions
Campos: id, user_id (FK para users), audio_path, feedback, score, created_at.
Relacionamentos: user.
Base (app/models/base.py)
Base declarativa para os modelos SQLAlchemy.
8. Schemas de Dados (Pydantic)
Os schemas Pydantic são usados para validação de dados de entrada e saída da API.

Lesson (app/schemas/lesson.py)
LessonBase: title, level, language, type, content.
LessonCreate: Herda de LessonBase.
LessonResponse: Herda de LessonBase, adiciona id.
Lesson (para lessons.py API): id, question_text, options, correct_option, type, media_url.
AnswerRequest: user_answer.
ChatRequest: messages, context.
ChatLog (app/schemas/chat_log.py)
ChatLogBase: user_id, message, response, lesson_id.
ChatLogCreate: Herda de ChatLogBase.
ChatLogResponse: Herda de ChatLogBase, adiciona id.
Auth (app/schemas/auth.py)
LoginRequest: email, password.
LoginResponse: access_token, token_type.
Token: access_token, token_type.
TokenData: user_id.
User (app/schemas/user.py)
UserBase: name, email, role, avatar_url.
UserCreate: Herda de UserBase, adiciona password.
UserLogin: email, password.
UserResponse: Herda de UserBase, adiciona id.
UserProfile: Herda de UserBase, adiciona id, language_progress.
Response (app/schemas/response.py)
WhisperFeedback: transcript, feedback, score.
LeaderboardEntry: user_id, name, avatar_url, score.
GenericResponse: success, message.
Progress (app/schemas/progress.py)
ProgressBase: lesson_id, user_id, completed, score.
ProgressCreate: Herda de ProgressBase.
ProgressResponse: Herda de ProgressBase, adiciona id.
9. Serviços e Utilitários
9.1. Serviços (app/services/)
feedback_engine.py:
generate_lesson_feedback(user_answer, correct_answer): Compara a resposta do usuário com a correta e gera feedback simples e pontuação.
whisper_service.py:
evaluate_speech_with_whisper(audio_path): Placeholder para a integração real com o modelo Whisper. Retorna transcrição, pontuação e feedback.
mistral_service.py:
chat_with_mistral(messages, context): Placeholder para a integração real com o modelo Mistral LLM. Simula uma resposta de chat.
leaderboard.py:
get_global_leaderboard(): Simula a recuperação de dados para o ranking global.
9.2. Utilitários (app/utils/)
token.py:
create_access_token(data): Gera um token JWT com base nos dados fornecidos.
verify_token(token): Verifica a validade de um token JWT.
helpers.py:
calculate_progress(completed, total): Calcula o percentual de progresso.
validate_audio_format(filename): Valida se o formato do arquivo de áudio é suportado.
10. Configuração da Aplicação
app/config.py:
Define configurações globais como PROJECT_NAME, API_VERSION.
DATABASE_URL: URL de conexão com o banco de dados (padrão SQLite, configurável via .env).
SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES: Configurações para JWT.
UPLOAD_DIR, AUDIO_MODEL_PATH, MISTRAL_MODEL_PATH: Caminhos para uploads e modelos de IA.
DEBUG: Modo de depuração.
11. Frontend (Mobile App - React Native)
11.1. Estrutura de Navegação
app/_layout.tsx (Layout Global):
Define o layout raiz da aplicação usando expo-router.
Gerencia o estado de autenticação (isLoggedIn) e redireciona para a tela de login se o usuário não estiver autenticado.
Configura o SafeAreaProvider e StatusBar.
Aplica o tema da aplicação (ThemeProvider do @react-navigation/native) com base no esquema de cores do sistema (useColorScheme).
app/(tabs)/_layout.tsx (Layout das Abas):
Define a navegação por abas (Tabs do expo-router).
Configura as opções de tela (cabeçalho oculto, cores da barra de abas, ícones).
Define as abas "Início" (index.tsx) e "Explorar" (explore.tsx) com seus respectivos ícones (Ionicons).
11.2. Telas Principais
app/(tabs)/index.tsx (Tela Inicial):
Exibe uma mensagem de boas-vindas ao Bilingui-AI.
Apresenta uma visão geral da plataforma e instruções básicas sobre como começar.
Utiliza ParallaxScrollView para um efeito visual no cabeçalho e Container para o conteúdo.
app/(tabs)/explore.tsx (Tela Explorar/Prática de Fala):
Focada na prática de fala.
Instrui o usuário a falar uma frase para receber transcrição e feedback.
Contém o VoiceButton para iniciar a gravação, FeedbackBox para exibir o feedback e XPProgressBar para mostrar o progresso.
screens/LoginScreen.tsx (Tela de Login):
Interface para o usuário inserir email e senha.
Contém TextInput para as credenciais e PrimaryButton para o login.
Implementa KeyboardAvoidingView para ajustar o layout quando o teclado aparece.
Lógica básica de validação de campos e um alert simulando o login.
screens/ProgressScreen.tsx (Tela de Progresso):
Exibe o progresso do usuário, incluindo XP, nível e conquistas.
Utiliza XPProgressBar e placeholders para "Conquistas" (badges).
Oferece um botão para "Exportar Histórico (PDF)" (funcionalidade futura).
screens/LessonScreen.tsx (Tela de Lição):
Exibe uma lista de questões de lição (FlatList).
Permite ao usuário selecionar opções de resposta e exibe feedback imediato.
Integração com getLesson do serviço de API para buscar as lições.
app/+not-found.tsx (Tela Não Encontrada):
Tela padrão para rotas não existentes.
11.3. Componentes Reutilizáveis (components/)
ParallaxScrollView.tsx: Um componente de rolagem que cria um efeito de paralaxe com uma imagem ou componente no cabeçalho.
Typography.tsx: Um componente de texto genérico para estilização consistente de diferentes tipos de texto (título, headline, padrão, secundário, link).
ThemedText.tsx: Uma versão de Typography que integra o esquema de cores do tema (Colors.ts) para garantir que o texto se adapte ao tema claro/escuro.
PrimaryButton.tsx: Um botão primário reutilizável com estilo adaptado ao tema.
Container.tsx: Um componente de contêiner básico que aplica um preenchimento e define a cor de fundo com base no tema.
FeedbackBox.tsx: Um componente para exibir feedback de correção de frases, incluindo a frase corrigida, explicação e uma frase alternativa.
XPProgressBar.tsx: Uma barra de progresso visual para exibir o XP e o nível do usuário.
VoiceButton.tsx: Um botão de microfone para iniciar/parar a gravação de áudio, com um indicador de atividade.
11.4. Constantes e Hooks (constants/, hooks/)
constants/Colors.ts: Define um objeto com as paletas de cores para os temas light e dark da aplicação.
hooks/useColorScheme.ts: Um hook React Native que retorna o esquema de cores do sistema ('light' ou 'dark').
hooks/useColorScheme.web.ts: Uma versão específica para web do useColorScheme que retorna 'light' fixo.
hooks/useThemeColor.ts: Um hook que retorna a cor apropriada com base no tema atual e no nome da cor especificado.
11.5. Serviço de API (Frontend)
service/api.ts:
getLesson(language, level): Função assíncrona que faz uma requisição GET para a API de backend (http://localhost:8000/llm/lesson) para buscar dados de lições. Utiliza axios.
12. Como Rodar Localmente
12.1. Pré-requisitos
Node.js e npm/yarn (para o Frontend)
Python 3.x e pip (para o Backend)
Expo CLI (para o Frontend)
Dispositivo móvel ou emulador/simulador para testar o app.
12.2. Passos para Configuração e Execução
Clonar o Repositório:

bash

Copiar
git clone <URL_DO_REPOSITORIO>
cd bilingui-AI
Configurar o Backend:

bash

Copiar
cd backend
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Configurar .env: Crie um arquivo .env na pasta backend/ com as variáveis de ambiente necessárias, por exemplo:

Copiar
DATABASE_URL="sqlite:///./bilingui.db"
SECRET_KEY="sua-chave-secreta-forte-aqui"
# Opcional: Caminhos para modelos de IA se você for rodá-los localmente
# AUDIO_MODEL_PATH="./models/whisper"
# MISTRAL_MODEL_PATH="./models/mistral"
Rodar Migrações (se houver): Se o projeto usar migrações com Alembic, você precisará executá-las:
bash

Copiar
alembic upgrade head
Iniciar o Servidor Backend:
bash

Copiar
uvicorn app.main:app --reload
O backend estará disponível em http://127.0.0.1:8000.
Configurar o Frontend:

bash

Copiar
cd ../frontend
npm install # ou yarn install
Iniciar o Aplicativo Expo:
bash

Copiar
npx expo start
Isso abrirá uma página no navegador com um QR code. Você pode escanear o QR code com o aplicativo Expo Go no seu celular ou usar um emulador/simulador.
13. Roadmap SCRUM (Visão Geral)
O projeto segue um roadmap ágil, dividido em Sprints com metas específicas:

Sprint 1: Autenticação de Usuário (Login com JWT).
Sprint 2: Implementação de Lições (leitura, fala, perguntas).
Sprint 3: Upload de Áudio e Transcrição via Whisper.
Sprint 4: Chat com IA via Mistral.
Sprint 5: Gamificação e Leaderboard.
Sprint 6: Estatísticas do Usuário e RadarChart.
Sprint 7: Multiplayer, Feedbacks aprimorados e Refatorações.
14. Contribuição
Contribuições são bem-vindas. O processo de contribuição segue o fluxo de trabalho padrão do Git:

Fork o projeto.
Crie um novo branch para sua feature (git checkout -b feature/nova-feature).
Faça seus commits seguindo um padrão (git commit -m "feat: nova feature x").
Envie suas alterações para o branch remoto (git push origin feature/nova-feature).
Abra um Pull Request (PR).
15. Licença
Este projeto está sob a licença MIT.