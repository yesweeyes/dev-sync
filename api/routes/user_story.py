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