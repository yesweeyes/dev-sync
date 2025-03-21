import os
import sys
from sqlalchemy import engine_from_config, pool
from alembic import context
from database import Base  # Ensure Base is correctly referenced

# Add the models directory to sys.path (so Alembic can find models)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import all models dynamically
from models import *  # This ensures all models are registered

# Alembic Config object
config = context.config

# Target metadata for migrations
target_metadata = Base.metadata

def run_migrations_online():
    """Run migrations in online mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()
