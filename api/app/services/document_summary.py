import uuid
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.document_summary import DocumentSummary
from app.schemas.document_summary import DocumentSummaryBase, DocumentSummaryCreate
from app.schemas.requirement_document import RequirementDocumentBase
from app.utils.requirement_document.parse_requirement_document import (
    parse_requirement_document as parse_requirement_document_util
)
from app.utils.document_summary.generate_document_summary import (
    generate_document_summary as generate_document_summary_util
)

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
