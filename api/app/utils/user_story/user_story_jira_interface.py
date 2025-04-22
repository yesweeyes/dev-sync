import uuid
import json
import requests
from requests.auth import HTTPBasicAuth
from sqlalchemy.orm import Session
from app.services.project import get_project
from app.services.user_story import get_user_story


def push_user_story_to_jira(user_story_id: uuid.UUID, db: Session):
    try:
        user_story = get_user_story(db, user_story_id)
        project_id = user_story.project_id
        project = get_project(db, project_id)

        PROJECT_KEY = project.jira_project_key
        JIRA_API_TOKEN = project.jira_project_auth
        JIRA_URL = project.jira_project_endpoint
        JIRA_EMAIL = project.jira_project_email

        auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
        headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        payload = json.dumps({
            "fields": {
                "project": {
                    "key": PROJECT_KEY
                },
                "summary": user_story.title,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": user_story.description + "/n" + user_story.acceptance_criteria
                                }
                            ]
                        }
                    ]
                },
                "issuetype": {
                    "name": user_story.issueType
                },
                "customfield_10016": user_story.storyPoints
            }
        })

        response = requests.post(
            JIRA_URL,
            data=payload,
            headers=headers,
            auth=auth
        )
        return response.json()
    except Exception as e:
        raise Exception(f"Unable to post user story to jira: {str(e)}")
    