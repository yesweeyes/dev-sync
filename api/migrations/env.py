import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from database import Base  # Import Base to access metadata

# Ensure models are imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Explicitly import models so Alembic can detect them
from models.project import Project  
from models.requirement_document import RequirementDocument  
from models.user_story import UserStory
from models.testcase import TestCase

# Alembic Config object
config = context.config

# Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Set target_metadata to Base.metadata
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""

    url = os.getenv("POSTGRES_DATABASE_URL", "postgresql://postgres:password@localhost:5432/devsync")
    config.set_main_option("sqlalchemy.url", url)
    context.configure(
        url=url,
        target_metadata=target_metadata,  # ✅ Ensure metadata is set
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()