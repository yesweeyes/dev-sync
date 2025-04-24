import uuid
import json
import requests
from requests.auth import HTTPBasicAuth
from sqlalchemy.orm import Session
from app.services.project import get_project
from app.services.testcases import get_test_case

def push_test_case_to_jira(test_case_id: uuid.UUID, db: Session):
    try:
        test_case = get_test_case(db, test_case_id)
        project_id = test_case.project_id
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
                "summary": test_case.module_name,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": test_case.description  + "/n" + test_case.post_condition
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
            JIRA_URL,
            data=payload,
            headers=headers,
            auth=auth
        )
        return response.json()
    except Exception as e:
        raise Exception(f"Unable to post user story to jira: {str(e)}")
    
