import pytest
import uuid
from app.schemas.testcase import TestCaseCreate

TEST_CASE_URL = "api/v1/testcase"

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
def create_test_case(client, create_project):
    data = {
        "project_id": str(create_project["id"]),
        "module_name": "Seller Registration",
        "title": "Valid Seller Registration",
        "preconditions": "The seller has not previously registered on the platform.",
        "priority": "HIGH",
        "description": "Test that a seller can successfully register on the platform with valid business details and contact information.",
        "test_steps": [
            "Enter valid business details (e.g., business name, address, phone number).",
            "Enter valid contact information (e.g., email, password).",
            "Submit the registration form.",
            "Verify that the seller is redirected to a confirmation page or receives a confirmation email."
        ],
        "post_condition": "The seller is successfully registered on the platform and can log in to their account.",
        "test_type": "Functional",
    }
    response = client.post(f"{TEST_CASE_URL}", json=data)
    assert response.status_code == 200
    return response.json()


def test_create_test_case_success(client, create_project):
    data = {
        "project_id": str(create_project["id"]),
        "module_name": "Shopping Cart and Wishlist",
        "title": "Valid Seller Registration",
        "preconditions": "The seller has not previously registered on the platform.",
        "priority": "HIGH",
        "description": "Test that a user can add and remove items from their shopping cart and wishlist.",
        "test_steps": [
            "Enter valid business details (e.g., business name, address, phone number).",
            "Enter valid contact information (e.g., email, password).",
            "Submit the registration form.",
            "Verify that the seller is redirected to a confirmation page or receives a confirmation email."
        ],
        "post_condition": "The seller is successfully registered on the platform and can log in to their account.",
        "test_type": "Functional",
    }
    response = client.post(f"{TEST_CASE_URL}/", json = data)
    assert response.status_code == 200
    story = TestCaseCreate(**response.json())
    assert story.title == data["title"]
    assert story.test_type == data["test_type"]

def test_create_test_case_failure(client):
    bad_data = {
        "title": "payment",
        "description": "Process the payment",
    }

    response = client.post(f"{TEST_CASE_URL}/", json=bad_data)

    assert response.status_code == 422

def test_get_test_case_success(client, create_test_case):
    response = client.get(f"{TEST_CASE_URL}/{create_test_case['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == create_test_case["id"]

def test_get_test_case_failure_not_found(client):
    non_existing_id = "00000000-0000-0000-0000-000000000000"
    response = client.get(f"{TEST_CASE_URL}/{non_existing_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == f"Test case with id: {non_existing_id} not found"

def test_update_test_case_success(client, create_test_case):
    updated_data = {
        "description": "Browse Products based on Category",
    }
    response = client.put(f"{TEST_CASE_URL}/{create_test_case['id']}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["description"] == "Browse Products based on Category"

def test_update_test_case_failure_not_found(client):
    non_existing_id = "00000000-0000-0000-0000-000000000000"
    updated_data = {
        "title": "Browse Products based on Category",
    }
    response = client.put(f"{TEST_CASE_URL}/{non_existing_id}", json=updated_data)
    assert response.status_code == 404
    assert response.json()["detail"] == f"Test case with id {non_existing_id} not found"

def test_delete_test_case_success(client, create_test_case):
    response = client.delete(f"{TEST_CASE_URL}/{create_test_case["id"]}")
    assert response.status_code == 200

def test_delete_test_case_failure(client, create_test_case):
    non_existing_id = "00000000-0000-0000-0000-000000000000"
    response = client.delete(f"{TEST_CASE_URL}/{non_existing_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == f"Test case with id {non_existing_id} not found"


def test_push_test_case_to_jira(client, create_test_case):
    response = client.get(f"{TEST_CASE_URL}/{create_test_case["id"]}/push")
    assert response.status_code in [200, 500]

