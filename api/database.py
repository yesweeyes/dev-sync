from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import POSTGRES_DATABASE_URL

# Create a synchronous engine
engine = create_engine(POSTGRES_DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
