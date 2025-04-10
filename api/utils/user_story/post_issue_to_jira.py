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


headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}


def create_jira_issue(story , auth_details):
    print(f"im inside:", auth_details)
    auth = HTTPBasicAuth(auth_details.jira_project_email, auth_details.jira_project_auth)
    payload = json.dumps({
        "fields": {
            "project": {
                "key": auth_details.jira_project_key
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
            "customfield_10016": story.storyPoints | 3
        }
    })

    response = requests.post(
        auth_details.jira_project_endpoint,
        data=payload,
        headers=headers,
        auth=auth
    )

    if response.status_code == 201:
        print(f"Story '{story.title}' created successfully.")
        return response
    else:
        print(f"Failed to create '{story.title}'. Error: {response.text}")

    
def parse_jira_issue(data, project_id:uuid.UUID, parent):
    project_id = project_id
    issue_id = data["id"]
    key = data["key"]
    end_point = data["self"]
    issue_type = getattr(parent, "issueType", "task")
    parent_id = parent.id

    return {
        "project_id":project_id,
        "issue_id":issue_id,
        "key":key,
        "end_point":end_point,
        "issue_type":issue_type,
        "parent_id" : parent_id
    }

def create_test_case_jira_issue(story , auth_details):
    print(f"im inside:", auth_details)
    auth = HTTPBasicAuth(auth_details.jira_project_email, auth_details.jira_project_auth)
    payload = json.dumps({
        "fields": {
            "project": {
                "key": auth_details.jira_project_key
            },
            "summary": story.module_name,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": story.description + "/n" + "/n" + story.post_condition
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": "Task"
            },
        }
    })

    response = requests.post(
        auth_details.jira_project_endpoint,
        data=payload,
        headers=headers,
        auth=auth
    )

    if response.status_code == 201:
        print(f"Story '{story.title}' created successfully.")
        return response
    else:
        print(f"Failed to create '{story.title}'. Error: {response.text}")