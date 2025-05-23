import uuid
import json
import fitz
from sqlalchemy.orm import Session
from langchain.chat_models import init_chat_model
from app.services.requirement_document import get_all_requirement_documents_for_project
from app.services.user_story import generate_create_user_story
from app.utils.user_story.user_story_structure import generate_user_story_helper
from app.config import GEMINI_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Groq Model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY)


def get_files(project_id: uuid.UUID, db: Session):  
    try:
        documents = get_all_requirement_documents_for_project(db, project_id)
        doc_list = [doc.file_path for doc in documents] if documents else []
        if not doc_list:
            print("No document found for this project ID.")
            return None
        return doc_list
    except Exception as e:
        raise Exception(f"Failed to get files for project: {str(e)}")


def extract_text_from_pdf(doc_list):
    text_chunks = []
    try:
        for doc_path in doc_list:
            document = fitz.open(doc_path)
            for page_num in range(document.page_count):
                page = document.load_page(page_num)
                text_chunks.append(page.get_text())
        return text_chunks
    except Exception as e:
        raise Exception(f"Failed to extract text from PDF: {str(e)}")


def generate_user_stories(summary, user_prompt):
    try:
        response = generate_user_story_helper(summary, user_prompt)
        return json.loads(response)
    except Exception as e:
        raise Exception(f"Failed to generate user stories: {str(e)}")


def insert_user_stories(db: Session, user_stories_json, project_id: uuid.UUID):
    try:
        for user_story in user_stories_json:
            parsed_story = {
                "project_id": project_id,
                "title": user_story["summary"],
                "description": user_story["description"],
                "acceptance_criteria": user_story["Acceptance Criteria"],
                "priority": user_story["Priority"].upper(),
                "storyPoints": user_story["storyPoints"],
                "labels": user_story["labels"],
                "issueType": user_story["issueType"]
            }
            generate_create_user_story(db, parsed_story)
    except Exception as e:
        raise Exception(f"Failed to insert user stories: {str(e)}")

