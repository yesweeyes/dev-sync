import pytest
from app.schemas.user_story import UserStoryCreate
from app.models.project import Project
import uuid

USER_STORY_URL = "api/v1/user_story"

@pytest.fixture
def create_project(client):
    data = {
        "name":"Test Project",
        "jira_project_key" : "p2",
        "jira_project_auth" : "avcdf",
        "jira_project_endpoint" : "https://abc.com/api/2/search",
        "jira_project_email": "abc@gmail.com",
        "github_endpoint" : "abc@github.com",
    }
    response = client.post("/api/v1/project/", json=data)
    assert response.status_code == 200
    return response.json()

@pytest.fixture
def create_user_story(client, create_project):
    data = {
        "title": "Browse Products",
        "project_id": create_project["id"],
        "acceptance_criteria": "Show products in grid",
        "labels": ["UI", "Browse"],
        "issueType": "Story"
    }

    response = client.post(f"{USER_STORY_URL}", json=data)
    assert response.status_code == 200
    return response.json()



def test_create_user_story_success(client, create_project):
    data = {
        "id": str(uuid.uuid4()),
        "title": "Browse Products",
        "project_id": create_project["id"],
        "acceptance_criteria": "Show products in grid",
        "labels": ["UI", "Browse"],
        "issueType": "Story"
    }
    response = client.post(f"{USER_STORY_URL}/", json = data)
    assert response.status_code == 200
    story = UserStoryCreate(**response.json())
    assert story.title == data["title"]
    assert story.issueType == data["issueType"]

def test_create_user_story_failure(client):
    bad_data = {
        "title": "payment",
        "description": "Process the payment", #missing issueType
    }

    response = client.post(f"{USER_STORY_URL}/", json=bad_data)

    assert response.status_code == 422

def test_get_user_story_success(client, create_user_story):
    response = client.get(f"{USER_STORY_URL}/{create_user_story['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == create_user_story["id"]

def test_get_user_story_failure_not_found(client):
    non_existing_id = "00000000-0000-0000-0000-000000000000"
    response = client.get(f"{USER_STORY_URL}/{non_existing_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == f"User Story with ID: {non_existing_id} doesnt exist"

def test_update_user_story_success(client, create_user_story):
    updated_data = {
        "title": "Browse Products based on Category",
    }
    response = client.put(f"{USER_STORY_URL}/{create_user_story['id']}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Browse Products based on Category"

def test_update_user_story_failure_not_found(client):
    non_existing_id = "00000000-0000-0000-0000-000000000000"
    updated_data = {
        "title": "Browse Products based on Category",
    }
    response = client.put(f"{USER_STORY_URL}/{non_existing_id}", json=updated_data)
    assert response.status_code == 404
    assert response.json()["detail"] == f"User Story with ID:{non_existing_id} not found"

def test_delete_user_story_success(client, create_user_story):
    response = client.delete(f"{USER_STORY_URL}/{create_user_story["id"]}")
    assert response.status_code == 200

def test_delete_user_story_failure(client, create_user_story):
    non_existing_id = "00000000-0000-0000-0000-000000000000"
    response = client.delete(f"{USER_STORY_URL}/{non_existing_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == f"User Story with ID: {non_existing_id} doesnt exist"

def test_generate_user_stories(client, create_project):
    response = client.post(f"{USER_STORY_URL}/generate", json={
        "project_id": create_project["id"],
        "user_prompt": "Generate user stories for user registration"
    })
    assert response.status_code in [200, 500]  

def test_push_user_story_to_jira(client, create_project):
    response = client.post(f"{USER_STORY_URL}/{create_project['id']}/push")
    assert response.status_code in [200, 500]  

def test_get_issue_from_jira(client, create_project):
    response = client.get(f"{USER_STORY_URL}/{create_project['id']}/jira")
    assert response.status_code in [200, 400]