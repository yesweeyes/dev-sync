#!/bin/bash

# Avoid re-initializing Alembic if the folder already exists
if [ ! -d "/code/migrations/versions" ]; then
  alembic init migrations
fi

# Generate a new migration only if one doesn't already exist
if [ -z "$(ls -A /code/migrations/versions)" ]; then
  alembic revision --autogenerate -m "init"
fi

# Apply migrations
alembic upgrade head

# Start FastAPI app
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
