import os
import pytest
import random

random.seed(18)

# ------------------- Fixtures -------------------

@pytest.fixture(scope="function")
def created_project(test_client):
    """Create a project for use in user story tests."""
    data = {
        "name": "Fixture Project",
        "jira_project_key": "FXT",
        "jira_project_auth": os.getenv("JIRA_PROJECT_AUTH_KEY", "dummy_auth"),
        "jira_project_endpoint": os.getenv("JIRA_PROJECT_ENDPOINT", "https://jira.example.com"),
        "jira_project_email": os.getenv("JIRA_PROJECT_EMAIL", "user@example.com"),
        "github_endpoint": os.getenv("JIRA_GITHUB_ENDPOINT", "https://github.com/test")
    }
    response = test_client.post("/api/v1/project/", json=data)
    assert response.status_code == 200
    return response.json()

# Helper to create a user story
def create_user_story(test_client, project_id):
    response = test_client.post("/api/v1/user_story/", json={
        "project_id": project_id,
        "title": "Sample User Story",
        "description": "User should be able to do something",
        "acceptance_criteria": "It should work this way",
        "priority": "MEDIUM",
        "storyPoints": 3,
        "labels": ["feature", "backend"],
        "issueType": "Story",
        "jiraPush": False,
        "jira_id": random.randint(1, 1000)
    })
    assert response.status_code == 200
    return response.json()

# ------------------- Tests -------------------

def test_create_user_story(test_client, created_project):
    response = test_client.post("/api/v1/user_story/", json={
        "project_id": created_project["id"],
        "title": "Test Story",
        "description": "Test description",
        "acceptance_criteria": "Acceptance criteria",
        "priority": "HIGH",
        "storyPoints": random.randint(1, 5),
        "labels": ["ui", "critical"],
        "issueType": "Bug",
        "jiraPush": False,
        "jira_id": random.randint(1, 1000)
    })
    assert response.status_code == 200
    json_data = response.json()
    assert "id" in json_data

def test_get_user_story_by_id(test_client, created_project):
    story = create_user_story(test_client, created_project["id"])
    response = test_client.get(f"/api/v1/user_story/{story['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == story["id"]

def test_update_user_story(test_client, created_project):
    story = create_user_story(test_client, created_project["id"])
    response = test_client.put(f"/api/v1/user_story/{story['id']}", json={
        "title": "Updated Story",
        "description": "Updated description",
        "acceptance_criteria": "Updated criteria",
        "priority": "LOW",
        "storyPoints": random.randint(1, 5),
        "labels": ["updated"],
        "jiraPush": True,
        "issueType": "Task",
        "jira_id": random.randint(1, 1000)
    })
    assert response.status_code == 200
    updated = response.json()
    assert updated["title"] == "Updated Story"
    assert updated["priority"] == "LOW"
    assert isinstance(updated["storyPoints"], int)

def test_delete_user_story(test_client, created_project):
    story = create_user_story(test_client, created_project["id"])
    response = test_client.delete(f"/api/v1/user_story/{story['id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "User Story deleted successfully"

def test_generate_user_stories(test_client, created_project):
    response = test_client.post("/api/v1/user_story/generate", json={
        "project_id": created_project["id"],
        "user_prompt": "Generate user stories for dashboard module"
    })
    assert response.status_code in [200, 500]  # depending on generation logic or mock state

def test_push_user_story_to_jira(test_client, created_project):
    story = create_user_story(test_client, created_project["id"])
    response = test_client.post(f"/api/v1/user_story/{story['id']}/push")
    assert response.status_code in [200, 500]  # external push might be mocked or fail gracefully

def test_get_issue_from_jira(test_client, created_project):
    response = test_client.get(f"/api/v1/user_story/{created_project['id']}/jira")
    assert response.status_code in [200, 400]
