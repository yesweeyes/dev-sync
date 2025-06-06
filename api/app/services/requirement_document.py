import os
import uuid
from fastapi import UploadFile, BackgroundTasks
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.models.requirement_document import RequirementDocument
from app.schemas.requirement_document import RequirementDocumentCreate, RequirementDocumentUpdate, RequirementDocumentBase
from app.services.document_summary import (
    create_document_summary_for_req_doc as create_document_summary_for_req_doc_service
)
from app.dependencies import REQUIREMENT_DOCS_FOLDER


def save_requirement_document(db: Session, project_id: uuid.UUID, file: UploadFile, background_tasks: BackgroundTasks):
    # Ensure uploads folder exists
    os.makedirs(REQUIREMENT_DOCS_FOLDER, exist_ok=True)

    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(REQUIREMENT_DOCS_FOLDER, unique_filename)

    # Read and save the file
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
        
    new_doc = RequirementDocument(
        project_id=project_id,
        original_name=file.filename,
        stored_name=unique_filename,
        file_path=file_path
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    # create_document_summary_for_req_doc_service(db, new_doc)
    background_tasks.add_task(create_document_summary_for_req_doc_service, db, new_doc)

    return new_doc

def get_requirement_document_by_id(db: Session, doc_id: uuid.UUID) -> RequirementDocument:
    doc = db.query(RequirementDocument).filter(RequirementDocument.id == doc_id).first()
    if not doc:
        raise NoResultFound(f"Requirement Document with ID {doc_id} not found")
    return doc

def get_all_requirement_documents_for_project(db: Session, project_id: uuid.UUID) -> List[RequirementDocument]:
    return db.query(RequirementDocument).filter(RequirementDocument.project_id == project_id).all()

def update_requirement_document(db: Session, doc_id: uuid.UUID, doc_data: RequirementDocumentUpdate) -> RequirementDocument:
    doc = db.query(RequirementDocument).filter(RequirementDocument.id == doc_id).first()
    if not doc:
        raise NoResultFound(f"Requirement Document with ID {doc_id} not found")
    
    for key, value in doc_data.model_dump(exclude_unset=True).items():
        setattr(doc, key, value)
    
    db.commit()
    db.refresh(doc)
    return doc

def delete_requirement_document(db: Session, doc_id: uuid.UUID) -> None:
    doc = db.query(RequirementDocument).filter(RequirementDocument.id == doc_id).first()
    if not doc:
        raise NoResultFound(f"Requirement Document with ID {doc_id} not found")

    db.delete(doc)
    db.commit()
