import uuid
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.schemas.user_story import UserStoryCreate, UserStoryUpdate, UserStoryGenerate
from app.database import get_db
from app.services.user_story import(
    create_user_story as create_user_story_service,
    get_user_story as get_user_story_service,
    update_user_story as update_user_story_service,
    delete_user_story as delete_user_story_service,
)
from app.services.document_summary import (
    get_document_summary_by_project as get_document_summary_by_project_service
)
import app.utils.user_story.generate_user_stories as user_story_gen_util
import app.utils.user_story.user_story_jira_interface as user_story_jira_interface_util
import app.utils.user_story.get_issue_from_jira as get_issue_from_jira_util

router = APIRouter(
    prefix = "/user_story",
    tags = ["user_story"],
)


@router.post("/")
def create_user_story(user_story: UserStoryCreate, db:Session = Depends(get_db)):
    try:
        return create_user_story_service(db, user_story)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{story_id}")
def get_user_story(story_id : uuid.UUID ,db:Session = Depends(get_db)):
    try:
        return get_user_story_service(db, story_id)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
@router.put("/{story_id}")
def update_user_story(story_id: uuid.UUID, story: UserStoryUpdate, db: Session = Depends(get_db)):
    try:
        return update_user_story_service(db, story_id, story)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
@router.delete("/{story_id}")
def delete_user_story(story_id: uuid.UUID, db:Session = Depends(get_db)):
    try:
        delete_user_story_service(db, story_id)
        return {"detail": "User Story deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
        
@router.post("/generate")
async def generate_stories(data: UserStoryGenerate, db: Session = Depends(get_db)):
    project_id = data.project_id
    user_prompt = data.user_prompt

    try:
        summary = get_document_summary_by_project_service(project_id=project_id)
        user_stories_json = user_story_gen_util.generate_user_stories(summary, user_prompt)
        user_story_gen_util.insert_user_stories(db, user_stories_json, project_id)
        
        return {"message": "User stories generated and stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/{user_story_id}/push")
def push_user_story_to_jira(user_story_id: uuid.UUID, db: Session =Depends(get_db)):
    try:
        jira_response = user_story_jira_interface_util.push_user_story_to_jira(user_story_id, db)
        return jira_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/{project_id}/jira")
def get_issue_from_jira(project_id: uuid.UUID, db: Session = Depends(get_db)):
    issues = get_issue_from_jira_util.get_story_issues_from_jira(db, project_id)
    try:
        for issue in issues:
            data = get_issue_from_jira_util.parse_issues(db, project_id, issue)
            res = create_user_story_service(db, data)
        return {"detail":"User Stories imported from JIRA"}
    except Exception as e:
        raise HTTPException(400, detail=str(e))
