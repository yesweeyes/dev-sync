import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.code_review import CodeReviewGenerate, CodeReviewUpdate
from database import get_db
from services.code_review import (
    generate_code_review_file as generate_code_review_service,
    get_code_review_file_by_id as get_code_review_file_by_id_service, 
    update_code_review_file as update_code_review_file_service,
    delete_code_review_file as delete_code_review_file_service
)

router = APIRouter(
    prefix="/code_review",
    tags=["code_review"],
)

@router.post("/generate")
async def generate_code_review(data: CodeReviewGenerate, db: Session = Depends(get_db)):
    project_id = data.project_id
    user_prompt = data.user_prompt
    try:
        return generate_code_review_service(db, project_id, user_prompt)
    except Exception as e:
        raise Exception(f"Failed to generate code review: {str(e)}")
    

@router.get("/{code_review_file_id}")
def get_code_review_file(code_review_file_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        return get_code_review_file_by_id_service(db, code_review_file_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{code_review_file_id}")
def update_code_review_file(code_review_file_id: uuid.UUID, data: CodeReviewUpdate, db: Session = Depends(get_db)):
    try:
        return update_code_review_file_service(db, code_review_file_id, data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{code_review_file_id}")
def delete_code_review_file(code_review_file_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        delete_code_review_file_service(db, code_review_file_id)
        return {"detail": "Code Review File deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))