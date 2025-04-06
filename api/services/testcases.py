from sqlalchemy.orm import Session
import uuid
from models.testcase import TestCase
from schemas.testcase import TestCaseCreate, TestCaseUpdate
from sqlalchemy.exc import NoResultFound
from typing import List

def create_test_case(db:Session, test_case_data:TestCaseCreate) -> TestCase:
    new_test_case = TestCase(**test_case_data)
    db.add(new_test_case)
    db.commit()
    db.refresh(new_test_case)
    return new_test_case

def get_test_case(db:Session, test_case_id: uuid.UUID) -> TestCase:
    test_case = db.query(TestCase).filter(TestCase.id == test_case_id).first()
    if not test_case:
        raise NoResultFound(f"Test case with id: {test_case_id} not found")
    return test_case

def get_all_test_cases(db:Session, project_id:uuid.UUID) -> List[TestCase]:
    return db.query(TestCase).filter(TestCase.project_id == project_id).all()

def update_test_case(db:Session, test_case_id:uuid.UUID, test_case_data:TestCaseUpdate) -> TestCase:
    test_case = db.query(TestCase).filter(TestCase.id == test_case_id).first()
    if not test_case:
        raise NoResultFound(f"Test case with id {test_case_id} not found")
    
    for key, value in test_case_data.model_dump(exclude_unset= True).items():
        setattr(test_case, key, value)
    
    db.commit()
    db.refresh(test_case)
    return test_case

def delete_test_case(db:Session, test_case_id:uuid.UUID) -> None:
    test_case = db.query(TestCase).filter(TestCase.id == test_case_id).first()
    if not test_case:
        raise NoResultFound(f"Test case with id {test_case_id} not found")
    db.delete(test_case)
    db.commit()


