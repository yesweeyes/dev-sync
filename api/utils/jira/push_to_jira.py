import os
import json
import requests
from requests.auth import HTTPBasicAuth
from schemas.project import ProjectBase
from schemas.push_to_jira import PushToJiraData


def push_to_jira(data: PushToJiraData, project: ProjectBase):
    """
    Abstraction to push entity to jira 
    """
    PROJECT_KEY = project.jira_project_key
    JIRA_URL = project.jira_project_endpoint
    JIRA_API_TOKEN = project.jira_project_auth
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
            "summary": data.summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": data.description
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": data.issueType
            },
        }
    })

    try:
        response = requests.post(
            JIRA_URL,
            data=payload,
            headers=headers,
            auth=auth
        )
        return response.json()
    
    except Exception as e:
        raise Exception(f"Unable to post data to jira: {str(e)}")
    

def add_attachment_to_issue(issue_key: str, file_path: str, project: ProjectBase):
    """
    Add attachment to valid issue in jira
    """
    JIRA_API_TOKEN = project.jira_project_auth
    JIRA_EMAIL = project.jira_project_email

    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

    headers = {
        "X-Atlassian-Token": "nocheck"
    }

    if not os.path.exists(file_path):
        raise Exception(f"File not found at path: {file_path}")

    payload = {
        "file": open(file_path, "rb"),
    }

    try:
        url = project.jira_project_endpoint
        url = url.rstrip("/") + f"/{issue_key}/attachments"
        print(url)
        response = requests.post(url, files=payload, headers=headers, auth=auth)
        if response.content:
            return response.json()
        else:
            return {"status_code": response.status_code, "text": response.text}
    except Exception as e:
        raise Exception (f"Unable to add attachment to issue:{issue_key}, \n {str(e)}")