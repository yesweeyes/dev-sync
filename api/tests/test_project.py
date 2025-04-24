import os
import pytest
from app.schemas.project import ProjectCreate

@pytest.fixture()
def project():
    project =  ProjectCreate(
        name="Test Project",
        jira_project_key="SCRUM",
        jira_project_auth=os.getenv("JIRA_PROJECT_AUTH_KEY"),
        jira_project_endpoint=os.getenv("JIRA_PROJECT_ENDPOINT"),
        jira_project_email=os.getenv("JIRA_PROJECT_EMAIL"),
        github_endpoint=os.getenv("JIRA_GITHUB_ENDPOINT")
    )
    
    return project

# --------------- Schema Validation Tests ----------------

def test_project_create_valid_data():
    data = {
        "name": "Test Project",
        "jira_project_key": "TPRJ",
        "jira_project_auth": "some_auth_token",
        "jira_project_endpoint": "https://jira.example.com",
        "jira_project_email": "user@example.com",
        "github_endpoint": "https://github.com/testproject"
    }
    project = ProjectCreate(**data)
    assert project.name == "Test Project"
    assert project.jira_project_email == "user@example.com"

def test_fixture_project_is_valid(project):
    assert isinstance(project, ProjectCreate)
    assert project.name == "Test Project"


def create_project(test_client):
    response = test_client.post("/api/v1/project/", json={
        "name": "Test Project",
        "jira_project_key": "SCRUM",
        "jira_project_auth": "token",
        "jira_project_endpoint": "https://jira.example.com",
        "jira_project_email": "user@example.com",
        "github_endpoint": "https://github.com/test"
    })
    assert response.status_code == 200
    return response.json()

def test_create_project(test_client):
    response = test_client.post("/api/v1/project/", json={
        "name": "New Project",
        "jira_project_key": "NP",
        "jira_project_auth": "auth_token",
        "jira_project_endpoint": "https://jira.new.com",
        "jira_project_email": "user@new.com",
        "github_endpoint": "https://github.com/new"
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_all_projects(test_client):
    create_project(test_client)
    response = test_client.get("/api/v1/project/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_project_by_id(test_client):
    project = create_project(test_client)
    response = test_client.get(f"/api/v1/project/{project['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == project["id"]

def test_update_project(test_client):
    project = create_project(test_client)
    response = test_client.put(f"/api/v1/project/{project['id']}", json={
        "name": "Updated Project",
        "jira_project_key": "UPD",
        "jira_project_auth": "newtoken",
        "jira_project_endpoint": "https://jira.updated.com",
        "jira_project_email": "updated@example.com",
        "github_endpoint": "https://github.com/updated"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Project"

def test_delete_project(test_client):
    project = create_project(test_client)
    response = test_client.delete(f"/api/v1/project/{project['id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Project deleted successfully"

def test_get_documents(test_client):
    project = create_project(test_client)
    response = test_client.get(f"/api/v1/project/{project['id']}/documents")
    assert response.status_code in [200, 404]

def test_get_user_stories(test_client):
    project = create_project(test_client)
    response = test_client.get(f"/api/v1/project/{project['id']}/user_stories")
    assert response.status_code in [200, 404]

def test_get_design_docs(test_client):
    project = create_project(test_client)
    response = test_client.get(f"/api/v1/project/{project['id']}/design_docs")
    assert response.status_code in [200, 404]

def test_get_test_cases(test_client):
    project = create_project(test_client)
    response = test_client.get(f"/api/v1/project/{project['id']}/test_cases")
    assert response.status_code in [200, 404]

def test_get_code_reviews(test_client):
    project = create_project(test_client)
    response = test_client.get(f"/api/v1/project/{project['id']}/code_reviews")
    assert response.status_code in [200, 404]
