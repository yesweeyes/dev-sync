from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models.project import Project
from schemas.project import ProjectCreate, ProjectUpdate
import uuid

def create_project(db: Session, project_data: ProjectCreate) -> Project:
    new_project = Project(**project_data.model_dump()) 
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

def get_project(db: Session, project_id: uuid.UUID) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise NoResultFound(f"Project with ID {project_id} not found")
    return project

def get_all_projects(db: Session) -> List[Project]:
    return db.query(Project).all()

def update_project(db: Session, project_id: uuid.UUID, project_data: ProjectUpdate) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise NoResultFound(f"Project with ID {project_id} not found")
    
    for key, value in project_data.model_dump(exclude_unset=True).items():
        setattr(project, key, value)
    
    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, project_id: uuid.UUID) -> None:
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise NoResultFound(f"Project with ID {project_id} not found")

    db.delete(project)
    db.commit()



