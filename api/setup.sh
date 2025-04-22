#!/bin/bash

# Wait for PostgreSQL to be ready (adjust the host and port if needed)
echo "Waiting for PostgreSQL to be ready..."
wait-for-it db:5432 --timeout=60 --strict -- echo "PostgreSQL is up"

# Check for migrations
alembic revision --autogenerate -m "init"

# Run Alembic migrations
alembic upgrade head

# Start the FastAPI app
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
