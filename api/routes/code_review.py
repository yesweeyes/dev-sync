from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.code_review import CodeReviewGenerate
from database import get_db
from services.code_review import (
    generate_code_review_file as generate_code_review_service
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
        generate_code_review_service(db, project_id, user_prompt)
        return {"message": "Code reviews generated and stored successfully."}
    except Exception as e:
        raise Exception(f"Failed to generate code review: {str(e)}")