from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.jira_issues import CreateJiraIssue
from database import get_db
import uuid
from requests.auth import HTTPBasicAuth
from services.project import get_project
from services.user_story import get_all_user_stories
from services.jira_issues import(
    create_jira_issue as create_jira_issue_service,
    get_all_jira_issues_by_project as get_all_jira_issues_by_project_service
)
import utils.user_story.post_issue_to_jira as issue
router = APIRouter(
    prefix="/issue",
    tags=["issue"]
)

@router.get("/{project_id}")
def post_issue(project_id:uuid.UUID, db:Session = Depends(get_db)):
    auth_details = get_project(db, project_id)
    auth = HTTPBasicAuth(auth_details.jira_project_email, auth_details.jira_project_auth)
    user_stories = get_all_user_stories(db, project_id)
    for story in user_stories:
        response = issue.create_jira_issue(story)
        if response:
            parsed_response = issue.parse_jira_issue(response, project_id)
            create_jira_issue_service(db, parsed_response)
            print("Inserted into db successfully")
        else:
            raise HTTPException(404, detail="Response is null")

