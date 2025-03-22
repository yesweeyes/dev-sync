from sqlalchemy.orm import Session
from models.project import Project
from schemas.project import ProjectSchema

def create_project(db: Session, project_data: ProjectSchema) -> Project:
    new_project = Project(**project_data.model_dump()) 
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project
