import uuid
import json
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.database import get_db
from app.services.user_story import get_all_user_stories as get_all_user_stories_service
from app.services.testcases import create_test_case
from app.services.document_summary import get_document_summary_by_project as get_document_summary_by_project_service
from app.utils.testcase.testcase_structure import generate_test_case_helper
    
db = next(get_db())
def generate_test_cases_for_user_stories(project_id:uuid.UUID, db:Session):
    user_stories = get_all_user_stories_service(db, project_id)
    if not user_stories:
        raise NoResultFound(f"Couldnt fetch user stories for project id : {project_id}")
    
    user_stories_list = [
    {
        "Title": story.title or "N/A",
        "Description": story.description or "N/A",
        "Acceptance Criteria": story.acceptance_criteria or "N/A",
        "Priority": story.priority or "N/A",
        "Story Points": story.storyPoints or "N/A",
        "Labels": story.labels or "N/A"
    }
    for story in user_stories
    ] 
    
    summary = get_document_summary_by_project_service(project_id)
    response = generate_test_case_helper(user_stories_list, summary)
    if response:
        return response
    else:
        raise NoResultFound(f"failed to generate testcases")


def store_test_cases_in_db(db: Session, test_case_response: str, project_id:uuid.UUID):
    test_cases = json.loads(test_case_response) 
    try:
        for list_of_test_cases in test_cases:
            for test_case in list_of_test_cases:
                parsed_testcase = {
                    "project_id" : project_id,
                    "module_name" : test_case["Module Name"],
                    "title" : test_case["Title"],
                    "description" : test_case["Description"],
                    "preconditions" : test_case["Preconditions"],
                    "test_steps" : test_case["Test Steps"],
                    "post_condition" : test_case["Post-condition"],
                    "priority" : test_case["Priority"].upper(),
                    "test_type" : test_case["Test Type"]
                }
                create_test_case(db, parsed_testcase)
    except Exception as e:
        raise NoResultFound(f"Failed to generate")

        


        
