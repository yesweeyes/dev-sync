from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.jira_issues import CreateJiraIssue
from database import get_db
import uuid
from requests.auth import HTTPBasicAuth
from services.project import get_project
from services.user_story import (
    get_all_user_stories as get_all_user_stories_service,
    get_user_story as get_user_story_service
)
from services.testcases import(
    get_all_test_cases as get_all_test_cases_service,
    get_test_case as get_test_case_service
)
from services.jira_issues import(
    create_jira_issue as create_jira_issue_service,
)
import utils.user_story.post_issue_to_jira as issue
router = APIRouter(
    prefix="/issue",
    tags=["issue"]
)

@router.get("/{project_id}/story")
def post_issue(project_id:uuid.UUID, db:Session = Depends(get_db)):
    auth_details = get_project(db, project_id)
    user_stories = get_all_user_stories_service(db, project_id)
    for story in user_stories:
        response = issue.create_jira_issue(story, auth_details)
        if response:
            response = response.json()
            parsed_response = issue.parse_jira_issue(response, project_id, story)
            print(parsed_response)
            create_jira_issue_service(db, parsed_response)
            print("Inserted into db successfully")
            return parsed_response
        else:
            raise HTTPException(404, detail="Response is null")

@router.get("/{story_id}/push")      
def post_issue_by_story_id(story_id:uuid.UUID, db:Session = Depends(get_db)):
    user_story = get_user_story_service(db, story_id)
    project_id = user_story.project_id
    auth_details = get_project(db, project_id)
    try:
        response = issue.create_jira_issue(user_story, auth_details)
        if response:
            response = response.json()
            parsed_response = issue.parse_jira_issue(response, project_id, user_story)
            create_jira_issue_service(db, parsed_response)
            print("Inserted into db successfully")
            return parsed_response
        else:
            raise HTTPException(404, detail="Response is null")
    except Exception as e:
        raise HTTPException(400, detail=str(e))
    

@router.get("/{project_id}/testcase")
def post_issue(project_id:uuid.UUID, db:Session = Depends(get_db)):
    auth_details = get_project(db, project_id)
    print(auth_details)
    test_cases = get_all_test_cases_service(db, project_id)
    print(len(test_cases))
    for test_case in test_cases:
        print("im inside")
        response = issue.create_test_case_jira_issue(test_case, auth_details, test_case)
        if response:
            response = response.json()
            parsed_response = issue.parse_jira_issue(response, project_id)
            create_jira_issue_service(db, parsed_response)
            print("Inserted into db successfully")
            return parsed_response
        else:
            raise HTTPException(404, detail="Response is null")

@router.get("/{testcase_id}/testcase/push")      
def post_issue_by_testcase_id(testcase_id:uuid.UUID, db:Session = Depends(get_db)):
    test_case = get_test_case_service(db, testcase_id)
    project_id = test_case.project_id
    auth_details = get_project(db, project_id)
    try:
        response = issue.create_test_case_jira_issue(test_case, auth_details)
        if response:
            response = response.json()
            parsed_response = issue.parse_jira_issue(response, project_id, test_case)
            create_jira_issue_service(db, parsed_response)
            print("Inserted into db successfully")
            return parsed_response
        else:
            raise HTTPException(404, detail="Response is null")
    except Exception as e:
        raise HTTPException(400, detail=str(e))
