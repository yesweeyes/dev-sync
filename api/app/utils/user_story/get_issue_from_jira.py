from sqlalchemy.orm import Session
import uuid
from models.user_story import UserStory
from requests.auth import HTTPBasicAuth
import requests
from services.project import get_project
from schemas.user_story import UserStoryCreate


def get_story_issues_from_jira(db:Session,project_id:uuid.UUID):
    auth_details = get_project(db, project_id)
    jira_endpoint = auth_details.jira_project_endpoint.split("api/3")[0]
    project_key = auth_details.jira_project_key

    url = f"{jira_endpoint}api/2/search"
    auth = HTTPBasicAuth(auth_details.jira_project_email, auth_details.jira_project_auth) 
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }    
    params = {
    "jql": f"project={project_key}"
    }
    response = requests.get(url, auth=auth, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        issues = data["issues"]
        if issues is None:
            return {"detail": "No issues found from Jira response."}

        jira_issues = [
            str(item.jira_id) for item in db.query(UserStory).filter(UserStory.project_id == project_id).all()
            if item.jiraPush
        ]
        
        new_issues = []
        for issue in issues:
            if issue["id"] not in jira_issues and issue["fields"]["issuetype"]["name"] == "Story":
                new_issues.append(issue)
        
        return new_issues
            
    else:
        print(f"Failed to fetch data: {response.status_code}")

def parse_issues(db: Session, project_id: uuid.UUID, issue: dict) -> UserStoryCreate:
    fields = issue.get("fields", {})

    return UserStoryCreate(
        project_id=project_id,
        title=fields.get("summary"),
        description=fields.get("description"),
        acceptance_criteria=None,
        priority=fields.get("priority", {}).get("name").upper() if fields.get("priority") else None,
        storyPoints=fields.get("customfield_10016"),
        labels=fields.get("labels", []),
        issueType=fields.get("issuetype", {}).get("name"),
        jiraPush = True,
        jira_id= issue["id"],
    )


