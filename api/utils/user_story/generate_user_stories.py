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
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

load_dotenv()
db = next(get_db())

def get_file(project_id: uuid.UUID, db: Session):   
    documents = get_all_requirement_documents_for_project(db, project_id)
    doc_list = []
    if not documents:
        print("No document found for this project ID.")
        return None
    
    for document in documents:
        doc_list.append(document.file_path)

    return doc_list


def extract_text_from_pdf(doc_list):
    text_chunks = []
    for doc_path in doc_list:
        document = fitz.open(doc_path)
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text = page.get_text()
            text_chunks.append(text)
    return text_chunks


def generate_user_stories(text_chunks):
    stories = []
    if text_chunks:
        for text in text_chunks:
            s = generate_user_story(content=text)
            stories.append(s)
        return stories
    else:
        return "Failed to extract text from URL"


def extract_json_blocks(stories):
    pattern = re.compile(r"\{(.*?)\}", re.DOTALL)
    matches = []
    for item in stories:
        matches.extend(pattern.findall(item))  
    return ["{" + match + "}" for match in matches]


def parse_user_story(data, project_id:uuid.UUID):
    title = data["summary"]
    description = data["description"]
    acceptance_criteria = data["Acceptance Criteria"]
    priority = data["Priority"].upper()
    story_points = data["storyPoints"]
    labels = data["labels"]
    issueType = data["issueType"]

    return {
        "project_id":project_id,
        "title": title,
        "description": description,
        "acceptance_criteria": acceptance_criteria,
        "priority": priority,
        "storyPoints": story_points,
        "labels": labels,
        "issueType": issueType
    }

def insert_user_stories(user_story_data, project_id:uuid.UUID):
    for story_data in user_story_data:
        story_data= json.loads(story_data)
        parsed_story = parse_user_story(story_data, project_id)
        create_user_story(db, parsed_story)
    print("Inserting into db is successful")
