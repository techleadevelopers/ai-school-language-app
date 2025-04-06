from logging.config import fileConfig
import os
import sys

from sqlalchemy import engine_from_config, pool
from alembic import context

# ✅ Adiciona o caminho da pasta raiz do projeto (para importar 'app')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import Base  # Base declarative
from app.models import user, lesson, progress, chat_log, audio_submission  # Importa todos os modelos

# Alembic Config
config = context.config

# Ativa logs
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Metadados dos modelos para autogenerate funcionar
target_metadata = Base.metadata

# 🔐 Lê URL do banco da variável de ambiente (fallback para .ini)
def get_url():
    return os.getenv("DATABASE_URL", config.get_main_option("sqlalchemy.url"))

def run_migrations_offline():
    """Rodar migrações no modo offline (sem conexão ativa)."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Rodar migrações no modo online (com engine ativa)."""
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# 🚀 Detecta modo
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
