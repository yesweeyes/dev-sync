import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.database import Base  # Import Base to access metadata
# Explicitly import models so Alembic can detect them
from app.models.project import Project  
from app.models.requirement_document import RequirementDocument  
from app.models.user_story import UserStory
from app.models.testcase import TestCase
from app.models.code_review import CodeReviewFile
from app.models.design_document import GeneratedHLDDocument, GeneratedLLDDocument
from app.models.document_summary import DocumentSummary


# Alembic Config object
config = context.config

# Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Set target_metadata to Base.metadata
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""

    url = os.getenv("POSTGRES_DATABASE_URL")
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
