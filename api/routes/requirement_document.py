from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
import uuid
from schemas.requirement_document import RequirementDocumentCreate, RequirementDocumentUpdate
from database import get_db
from services.requirement_document import (
    save_requirement_document as save_requirement_document_service,
    get_requirement_document_by_id,
    update_requirement_document as update_doc_service,
    delete_requirement_document as delete_doc_service
)

router = APIRouter(
    prefix="/document",
    tags=["document"],
)

@router.post("/{project_id}/upload")
def upload_document(project_id: uuid.UUID, file: UploadFile = File(...), db: Session = Depends(get_db)):
    print("Here!!!!!!!!!!")
    try:
        return save_requirement_document_service(db, project_id, file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{doc_id}")
def get_requirement_document(doc_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        return get_requirement_document_by_id(db, doc_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{doc_id}")
def update_requirement_document(doc_id: uuid.UUID, doc: RequirementDocumentUpdate, db: Session = Depends(get_db)):
    try:
        return update_doc_service(db, doc_id, doc)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{doc_id}")
def delete_requirement_document(doc_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        delete_doc_service(db, doc_id)
        return {"detail": "Requirement Document deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
