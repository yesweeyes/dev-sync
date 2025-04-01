from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from schemas.user_story import CreateUserStory, UpdateUserStory
from database import get_db
import uuid
import os
from fastapi.responses import FileResponse
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

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True) 

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
            doc_list = story.get_file(project_id, db)
            text_chunks = story.extract_text_from_pdf(doc_list)
            stories = story.generate_user_stories(text_chunks)
            json_data = story.extract_json_blocks(stories)
            story.insert_user_stories(json_data, project_id)
            userStories = get_all_user_stories(project_id, db)
            return userStories
        else:
            return get_all_user_stories(project_id, db)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
@router.get("/userStories/download/{project_id}")
def download_user_stories(project_id:uuid.UUID, db:Session = Depends(get_db)):
    userStories = get_all_user_stories(project_id, db)
    if not userStories:
        raise HTTPException(status_code=404, detail=f"No user stories found for project {project_id}")
    try:
        unique_filename = f"{project_id}_UserStories.txt"
        file_path = os.path.join(DOWNLOAD_FOLDER, unique_filename)
        with open(file_path, "w", encoding="utf-8") as file:
            for story in userStories:
                file.write(
                    f"User Story:\n"
                    f"Title: {story.title or 'N/A'}\n"
                    f"Description: {story.description or 'N/A'}\n"
                    f"Acceptance Criteria: {story.acceptance_criteria or 'N/A'}\n"
                    f"Priority: {story.priority or 'N/A'}\n"
                    f"Story Points: {story.storyPoints or 'N/A'}\n"
                    f"Labels: {story.labels or 'N/A'}\n"
                    f"{'-'*40}\n\n" 
                )
        return FileResponse(
            path=file_path,
            media_type="application/octet-stream",
            filename=unique_filename,
            headers={"Content-Disposition": f"attachment; filename={unique_filename}"}
        )
    except Exception as e:
        raise HTTPException(400, detail=f"Error fetching user stories: {str(e)}")
