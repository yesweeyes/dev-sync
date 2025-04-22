import uuid
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.schemas.testcase import TestCaseCreate, TestCaseUpdate
from app.database import get_db
import app.utils.test_case.generate_test_cases as test_case_service
from app.services.testcases import(
    create_test_case as create_test_case_service,
    get_test_case as get_test_case_service,
    update_test_case as update_test_case_service,
    delete_test_case as delete_test_case_service
)
import app.utils.test_case.test_case_jira_interface as test_case_jira_interface_service


router = APIRouter(
    prefix="/testcase",
    tags=["testcase"]
)

@router.post("/")
def create_test_case(test_case_data: TestCaseCreate, db:Session = Depends(get_db)):
    try:
        return create_test_case_service(db, test_case_data)
    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))
    
@router.get("/{test_case_id}")
def get_test_case(test_case_id:uuid.UUID, db:Session = Depends(get_db)):
    try:
        return get_test_case_service(db, test_case_id)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
@router.put("/{test_case_id}", response_model=TestCaseUpdate)
def update_test_case(test_case_id:uuid.UUID, test_case_data:TestCaseUpdate,db:Session = Depends(get_db)):
    try:
        return update_test_case_service(db, test_case_id, test_case_data)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
@router.delete("/{test_case_id}")
def delete_test_case(test_case_id:uuid.UUID, db:Session = Depends(get_db)):
    try:
        return delete_test_case_service(db, test_case_id)
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
        
@router.post("/{project_id}/generate")
async def generate_test_cases(project_id:uuid.UUID, db:Session = Depends(get_db)):
    try:
        response = test_case_service.generate_test_cases_for_user_stories(project_id, db)
        test_case_service.store_test_cases_in_db(db, response, project_id)

        return {"message": "Test cases saved to database successfully"}
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
@router.get("/{test_case_id}/push")
def push_test_case_to_jira(test_case_id:uuid.UUID, db:Session = Depends(get_db)):
    try:
        jira_response =  test_case_jira_interface_service.push_test_case_to_jira(test_case_id, db)
        return jira_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
