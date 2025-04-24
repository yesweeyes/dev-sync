import os
from dotenv import load_dotenv
import pytest
from pydantic import ValidationError
from app.schemas.project import ProjectCreate

load_dotenv()

@pytest.fixture()
def project():
    project_data = {
        "name": "Test Project",
        "jira_project_key": "SCRUM",
        "jira_project_auth": os.getenv("JIRA_PROJECT_AUTH_KEY"),
        "jira_project_endpoint": os.getenv("JIRA_PROJECT_ENDPOINT"),
        "jira_project_email": os.getenv("JIRA_PROJECT_EMAIL"),
        "github_endpoint": os.getenv("JIRA_GITHUB_ENDPOINT")
    }

    project = ProjectCreate(**project_data)
    return project

def test_project_create_valid_data():
    project_data = {
        "name": "Test Project",
        "jira_project_key": "TPRJ",
        "jira_project_auth": "some_auth_token",
        "jira_project_endpoint": "https://jira.example.com",
        "jira_project_email": "user@example.com",
        "github_endpoint": "https://github.com/testproject"
    }

    project = ProjectCreate(**project_data)
    
    assert project.name == "Test Project"
    assert project.jira_project_key == "TPRJ"
    assert project.jira_project_auth == "some_auth_token"
    assert project.jira_project_endpoint == "https://jira.example.com"
    assert project.jira_project_email == "user@example.com"
    assert project.github_endpoint == "https://github.com/testproject"

