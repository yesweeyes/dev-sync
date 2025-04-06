from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models.requirement_document import RequirementDocument
from schemas.requirement_document import RequirementDocumentCreate, RequirementDocumentUpdate, RequirementDocumentBase
import uuid
from fastapi import UploadFile
from typing import List
import os

UPLOAD_FOLDER = "uploads"

def save_requirement_document(db: Session, project_id: uuid.UUID, file: UploadFile):
    # Ensure uploads folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)

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
