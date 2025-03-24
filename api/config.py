from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
POSTGRES_DATABASE_URL = os.getenv("POSTGRES_DATABASE_URL")
VECTOR_MICROSERVICE_URL=os.getenv("VECTOR_MICROSERVICE_URL")