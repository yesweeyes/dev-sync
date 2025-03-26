from dotenv import load_dotenv
from database import get_db
from sqlalchemy.orm import Session
import uuid
from services.project import get_project
from services.user_story import get_all_user_stories
from requests.auth import HTTPBasicAuth
import requests
import json

load_dotenv()
db = next(get_db())
project_id = uuid.UUID("7b1d790a-1daf-41ac-95fd-f453fac87348")

def get_auth_details(project_id: uuid.UUID, db: Session):
    auth_details = get_project(db, project_id)
    return auth_details
auth_details = get_auth_details(project_id, db)

JIRA_API_TOKEN = auth_details.jira_project_auth
JIRA_URL = auth_details.jira_project_endpoint
PROJECT_KEY = auth_details.jira_project_key
JIRA_EMAIL = auth_details.jira_project_email

print(f"api:", JIRA_API_TOKEN)
print(f"email", JIRA_EMAIL)
print(f"ednpoint:", JIRA_URL)

auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

def user_story_details(project_id: uuid.UUID, db: Session):
    issue_details = get_all_user_stories(db, project_id)
    return issue_details

issue_details = user_story_details(project_id, db)

def create_jira_issue(story):
    payload = json.dumps({
        "fields": {
            "project": {
                "key": PROJECT_KEY
            },
            "summary": story.title,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": story.description + "/n" + story.acceptance_criteria
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": story.issueType
            },
            "customfield_10016": story.storyPoints
        }
    })

    response = requests.post(
        JIRA_URL,
        data=payload,
        headers=headers,
        auth=auth
    )

    if response.status_code == 201:
        print(f"Story '{story.title}' created successfully.")
    else:
        print(f"Failed to create '{story.title}'. Error: {response.text}")

# for issue in issue_details:
#     #create_jira_issue(issue)
    
