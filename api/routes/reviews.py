import os
import uuid
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from database import get_db
from services.code_review import (
    get_code_review_file_by_id as get_code_review_file_by_id_service
)
from services.project import (
    get_project as get_project_service
)
from utils.code_review import (
    push_to_jira as code_review_push_to_jira_util
)

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
)

@router.get("/{filename}")
def serve_file(filename: str):
    file_path = os.path.join("reviews", filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    # Determine media type based on file extension
    ext = os.path.splitext(filename)[1].lower()
    media_types = {
        '.html': 'text/html',
        '.htm': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.json': 'application/json',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.svg': 'image/svg+xml',
    }
    media_type = media_types.get(ext, 'application/octet-stream')

    return FileResponse(file_path, media_type=media_type)


@router.post("/{code_review_id}/push")
def push_coder_review_to_jira(code_review_id: uuid.UUID, db: Session=Depends(get_db)):
    code_review = get_code_review_file_by_id_service(db, code_review_id)
    project_id = code_review.project_id
    project = get_project_service(db, project_id)
    
    return code_review_push_to_jira_util(code_review, project)