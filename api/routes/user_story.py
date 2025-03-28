from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from schemas.user_story import CreateUserStory, UpdateUserStory
from database import get_db
import uuid
from services.user_story import(
    create_user_story as create_user_story_service,
    get_user_story as get_user_story_service,
    get_all_user_stories as get_all_user_stories_service,
    update_user_story as update_user_story_service,
    delete_user_story as delete_user_story_service,
)
import UserStories.generate_user_stories as story
router = APIRouter(
    prefix = "/story",
    tags = ["story"],
)

@router.get("/{project_id}")
def get_all_user_stories(project_id : uuid.UUID ,db:Session = Depends(get_db)):
    try:
        return get_all_user_stories_service(db, project_id)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
@router.post("/{project_id}/post")
def create_user_story(story : CreateUserStory, db:Session = Depends(get_db)):
    try:
        return create_user_story_service(db, story)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/story/{story_id}")
def get_user_story(story_id : uuid.UUID ,db:Session = Depends(get_db)):
    try:
        return get_user_story_service(db, story_id)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
@router.put("/{story_id}")
def upadte_user_story(story_id: uuid.UUID, story:UpdateUserStory, db: Session = Depends(get_db)):
    try:
        return update_user_story_service(db, story_id, story)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
@router.delete("/{story_id}")
def delete_user_story(story_id:uuid.UUID, db:Session = Depends(get_db)):
    try:
        return delete_user_story_service(db, story_id)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
@router.get("/userStories/{project_id}")
def generate_stories(project_id: uuid.UUID, db:Session = Depends(get_db)):
    try:
        if not get_all_user_stories(project_id, db):
            file_path = story.get_file(project_id, db)
            print("file path retrieved")
            text_chunks = story.extract_text_from_pdf(file_path)
            print("data divided into chunks")
            stories = story.generate_user_stories(text_chunks)
            print("user stories generated")
            json_data = story.extract_json_blocks(stories)
            print("converted into json")
            story.insert_user_stories(json_data, project_id)
            print("inserted into db")
            userStories = get_all_user_stories(project_id, db)
            print("Inserting into db is succesful")
            return userStories
        else:
            return get_all_user_stories(project_id, db)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
