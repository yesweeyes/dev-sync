from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models.user_story import UserStory
from schemas.user_story import UserStoryCreate, UserStoryUpdate
import uuid
from typing import List
from fastapi.responses import FileResponse
import os
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True) 

def create_user_story(db:Session, user_story_data: UserStoryCreate) -> UserStory:
    new_story = UserStory(**user_story_data.model_dump())
    db.add(new_story)
    db.commit()
    db.refresh(new_story)
    return new_story

# Function called by generate user stories from llm
def generate_create_user_story(db:Session, user_story_data: UserStoryCreate) -> UserStory:
    new_story = UserStory(**user_story_data)
    db.add(new_story)
    db.commit()
    db.refresh(new_story)
    return new_story

def get_user_story(db:Session, story_id: uuid.UUID) -> UserStory:
    user_story = db.query(UserStory).filter(UserStory.id == story_id).first()
    if not user_story:
        raise NoResultFound(f"User Story with ID: {story_id} doesnt exist")
    return user_story

def get_all_user_stories(db:Session, project_id:uuid.UUID) -> List[UserStory]:
    return db.query(UserStory).filter((UserStory.project_id == project_id) & or_(UserStory.jira_ignored == False, UserStory.jira_ignored == None)).all()

def update_user_story(db:Session, story_id:uuid.UUID, user_story_data: UserStoryUpdate) -> UserStory:
    user_story = db.query(UserStory).filter(UserStory.id == story_id).first()
    if not user_story:
        raise NoResultFound(f"User Story with ID:{story_id} not found")
        
    for key, value in user_story_data.model_dump(exclude_unset = True).items():
        setattr(user_story, key, value)
        
    db.commit()
    db.refresh(user_story)
    return user_story

def delete_user_story(db:Session, story_id:uuid.UUID) -> None:
    user_story = db.query(UserStory).filter(UserStory.id == story_id).first()
    if not user_story:
        raise NoResultFound(f"User Story with ID: {story_id} doesnt exist")
    db.delete(user_story)
    db.commit()

