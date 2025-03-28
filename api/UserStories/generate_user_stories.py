from groq import Groq
from sqlalchemy.orm import Session
import uuid
import re
import json
import fitz
from dotenv import load_dotenv
from database import get_db
from models import user_story
from UserStories.user_story_structure import generate_user_story
from services.requirement_document import get_all_requirement_documents_for_project
from services.user_story import create_user_story

load_dotenv()
db = next(get_db())

def get_file(project_id: uuid.UUID, db: Session):   
    document = get_all_requirement_documents_for_project(db, project_id)
    if document:
        return document.file_path
    else:
        print("No document found for this project ID.")

# file_path = get_file(project_id,db)

def extract_text_from_pdf(file_path):
    document = fitz.open(file_path)
    text_chunks = []
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text = page.get_text()
        text_chunks.append(text)
    return text_chunks

# text_chunks = extract_text_from_pdf(file_path)
# print(f'text chunks list size:', len(text_chunks))

def generate_user_stories(text_chunks):
    stories = []
    if text_chunks:
        for text in text_chunks:
            s = generate_user_story(content=text)
            stories.append(s)
        return stories
    else:
        return "Failed to extract text from URL"

# stories = generate_user_stories(text_chunks)

def extract_json_blocks(stories):
    pattern = re.compile(r"\{(.*?)\}", re.DOTALL)
    matches = []
    for item in stories:
        matches.extend(pattern.findall(item))  
    return ["{" + match + "}" for match in matches]

# json_obj = extract_json_blocks(stories)

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
        
# insert_user_stories(json_obj)