import os
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import get_db, Base
from app.schemas.project import ProjectCreate

load_dotenv()

# Use a different database URL for testing
TEST_DATABASE_URL = os.getenv("POSTGRES_TEST_DATABASE_URL")

# Set up the test engine and session
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables before tests
Base.metadata.create_all(bind=engine)

# Dependency override for test DB session
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Apply the override
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="session")
def test_db():
    # Optional: truncate tables or drop/create all before running tests
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)  # Clean up after tests

@pytest.fixture(scope="session")
def test_client(test_db):
    with TestClient(app) as client:
        yield client