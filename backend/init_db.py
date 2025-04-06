from app.database import Base, engine
from app.models import user, lesson, progress, chat_log, audio_submission

print("🛠️ Criando todas as tabelas...")
Base.metadata.create_all(bind=engine)
print("✅ Pronto!")
