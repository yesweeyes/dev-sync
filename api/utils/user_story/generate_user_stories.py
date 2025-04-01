from groq import Groq
from sqlalchemy.orm import Session
import uuid
import re
import json
import fitz
from dotenv import load_dotenv
from database import get_db
from models import user_story
from utils.user_story.user_story_structure import generate_user_story
from services.requirement_document import get_all_requirement_documents_for_project
from services.user_story import create_user_story
import os
import getpass
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

# Load Groq API Key
if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

# Initialize Groq Model
model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")


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


def generate_user_stories(text_chunks, user_prompt):
    try:
        if not text_chunks:
            return []
        
        system_template = """
        You are an AI specialized in generating user stories. Maintain context across multiple inputs.
        At the end, return an array of user stories in JSON format, following this structure:
        {example_output}
        """

        example_output = """
        [{
            "summary": "User Registration",
            "description": "As a new user, I want to register an account so that I can access the platform.",
            "Acceptance Criteria": "The user should be able to enter their details (name, email, password).",
            "issueType": "Story",
            "labels": ["authentication", "user-management"],
            "storyPoints": 3,
            "Priority": "High"
        }]
        """

        messages = [SystemMessage(content=system_template.format(example_output=example_output))]
        
        for chunk in text_chunks:
            messages.append(HumanMessage(content=chunk))
        
        messages.append(HumanMessage(content=user_prompt))
        
        response = model.invoke(messages)
        return json.loads(response.content)
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
            create_user_story(db, parsed_story)
    except Exception as e:
        raise Exception(f"Failed to insert user stories: {str(e)}")

