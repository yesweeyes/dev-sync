import uuid
from fastapi import Depends
from pydantic import UUID4
from sqlalchemy.orm import Session
from models.document_summary import DocumentSummary
from schemas.document_summary import DocumentSummaryBase, DocumentSummaryCreate
from schemas.requirement_document import RequirementDocumentBase
from utils.requirement_document.parse_requirement_document import (
    parse_requirement_document as parse_requirement_document_util
)
from utils.document_summary.generate_document_summary import (
    generate_document_summary as generate_document_summary_util
)
from database import SessionLocal

# Take a Requirement Doc File and create a summary in db
def create_document_summary_for_req_doc(db: Session, file: RequirementDocumentBase) -> DocumentSummary:
    document_id = file.id
    project_id = file.project_id

    document_content = parse_requirement_document_util(file=file)
    summary = generate_document_summary_util(documet_content=document_content)

    document_summary = {
        "project_id": project_id,
        "document_id": document_id,
        "summary": summary,
    }

    document_summary = DocumentSummary(**document_summary)
    
    db.add(document_summary)
    db.commit()
    db.refresh(document_summary)
    
    return document_summary

def get_document_summary_by_project(project_id: uuid.UUID) -> str:
    db = SessionLocal()  
    summaries = db.query(DocumentSummary).filter(DocumentSummary.project_id==project_id).all()
    summary_text = "\n".join([summary.summary for summary in summaries])
    return summary_text
