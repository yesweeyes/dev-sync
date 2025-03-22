from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.project import ProjectSchema
from database import get_db
from services.project import create_project as create_project_service

router = APIRouter(
    prefix="/project",
    tags=["project"],
)

@router.post("/")
def create_project(project: ProjectSchema, db: Session = Depends(get_db)):
    return create_project_service(db, project)
