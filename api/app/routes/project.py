import uuid
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.database import get_db
from app.services.project import (
    create_project as create_project_service,
    get_all_projects as get_all_projects_service,
    get_project as get_project_service,
    update_project as update_project_service,
    delete_project as delete_project_service,
)
from app.services.requirement_document import (
    get_all_requirement_documents_for_project as get_project_documents_service
)
from app.services.user_story import (
    get_all_user_stories as get_all_user_stories_service,
)
from app.services.testcases import (
    get_all_test_cases as get_all_test_cases_service,
)
from app.services.code_review import (
    get_all_code_review_file_for_project as get_all_code_review_file_service
)

from app.services.design_doc import (
    get_all_design_documents as get_all_design_documents_service
)

router = APIRouter(
    prefix="/project",
    tags=["project"],
)

@router.get("/")
def get_all_projects(db: Session = Depends(get_db)):
    return get_all_projects_service(db)

@router.post("/")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project_service(db, project)

@router.get("/{project_id}")
def get_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        project = get_project_service(db, project_id)
        return project
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.put("/{project_id}")
def update_project(project_id: uuid.UUID, project: ProjectUpdate, db: Session = Depends(get_db)):
    try:
        return update_project_service(db, project_id, project)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{project_id}")
def delete_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        delete_project_service(db, project_id)
        return {"detail": "Project deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{project_id}/documents")
def get_documents(project_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        documents =  get_project_documents_service(db, project_id)
        return documents
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/{project_id}/user_stories")
def get_user_stories(project_id : uuid.UUID, db:Session = Depends(get_db)):
    try:
        return get_all_user_stories_service(db, project_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail = str(e))
    
@router.get("/{project_id}/design_docs")
def get_design_docs(project_id: uuid.UUID, db:Session = Depends(get_db)):
    try:
        return get_all_design_documents_service(db, project_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/{project_id}/test_cases")
def get_all_test_cases(project_id:uuid.UUID, db:Session = Depends(get_db)):
    try:
        return get_all_test_cases_service(db, project_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/{project_id}/code_reviews")
def get_all_code_reviews(project_id:uuid.UUID, db:Session = Depends(get_db)):
    try:
        return get_all_code_review_file_service(db, project_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
# @router.get("/{project_id}/jira")
# def get_issue_from_jira(project_id: uuid.UUID, db: Session = Depends(get_db)):
#     issues = get_issue_from_jira_util.get_story_issues_from_jira(db, project_id)
#     try:
#         for issue in issues:
#             data = get_issue_from_jira_util.parse_issues(db, project_id, issue)
#             res = create_user_story_service(db, data)
#         return {"detail":"User Stories imported from JIRA"}
#     except Exception as e:
#         raise HTTPException(400, detail=str(e))

