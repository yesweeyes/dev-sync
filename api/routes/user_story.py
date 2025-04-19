from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from schemas.user_story import UserStoryCreate, UserStoryUpdate, UserStoryGenerate
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
    download_user_stories as download_user_stories_service
)
import utils.user_story.generate_user_stories as user_story_gen_util
import utils.user_story.user_story_jira_interface as user_story_jira_interface_util
import utils.user_story.get_issue_from_jira as get_issue_from_jira_util

router = APIRouter(
    prefix = "/user_story",
    tags = ["user_story"],
)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


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
        return delete_user_story_service(db, story_id)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
        
@router.post("/generate")
def generate_stories(data: UserStoryGenerate, db: Session = Depends(get_db)):
    project_id = data.project_id
    user_prompt = data.user_prompt

    try:
        documents = user_story_gen_util.get_files(project_id, db)
        if not documents:
            raise HTTPException(status_code=404, detail="No requirement documents found for the given project ID.")
        
        text_chunks = user_story_gen_util.extract_text_from_pdf(documents)
        user_stories_json = user_story_gen_util.generate_user_stories(text_chunks, user_prompt)
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
            print(res)
        return f"Data obtained successfully"
    except Exception as e:
        raise HTTPException(400, detail=str(e))
    
# @router.get("/userStories/download/{project_id}")
# def download_user_stories(project_id:uuid.UUID, db:Session = Depends(get_db)):
#     try:
#         return download_user_stories_service(db, project_id)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    

# TODO: Move the logic to project router and fine tune the code  
# @router.get("/userStories/download/{project_id}")
# def download_user_stories(project_id:uuid.UUID, db:Session = Depends(get_db)):
#     userStories = get_all_user_stories(project_id, db)
#     if not userStories:
#         raise HTTPException(status_code=404, detail=f"No user stories found for project {project_id}")
#     try:
#         unique_filename = f"{project_id}_UserStories.txt"
#         file_path = os.path.join(DOWNLOAD_FOLDER, unique_filename)
#         with open(file_path, "w", encoding="utf-8") as file:
#             for story in userStories:
#                 file.write(
#                     f"User Story:\n"
#                     f"Title: {story.title or 'N/A'}\n"
#                     f"Description: {story.description or 'N/A'}\n"
#                     f"Acceptance Criteria: {story.acceptance_criteria or 'N/A'}\n"
#                     f"Priority: {story.priority or 'N/A'}\n"
#                     f"Story Points: {story.storyPoints or 'N/A'}\n"
#                     f"Labels: {story.labels or 'N/A'}\n"
#                     f"{'-'*40}\n\n" 
#                 )
#         return FileResponse(
#             path=file_path,
#             media_type="application/octet-stream",
#             filename=unique_filename,
#             headers={"Content-Disposition": f"attachment; filename={unique_filename}"}
#         )
#     except Exception as e:
#         raise HTTPException(400, detail=f"Error fetching user stories: {str(e)}")
