import uuid
from typing import List, Union
from sqlalchemy.orm import Session
from app.models.design_document import GeneratedHLDDocument,GeneratedLLDDocument
from sqlalchemy.exc import NoResultFound

def get_all_design_documents(db:Session, project_id:uuid.UUID) -> List[Union[GeneratedHLDDocument,GeneratedLLDDocument]]:
    hld_documents=db.query(GeneratedHLDDocument).filter(GeneratedHLDDocument.project_id == project_id).all()
    lld_documents=db.query(GeneratedLLDDocument).filter(GeneratedLLDDocument.project_id == project_id).all()

    return hld_documents+lld_documents

def delete_design_documents(db:Session, design_docs_file_id:uuid.UUID):
    doc=db.query(GeneratedHLDDocument).filter(GeneratedHLDDocument.id== design_docs_file_id).first()

    if not doc:
        doc =db.query(GeneratedLLDDocument).filter(GeneratedLLDDocument.id==design_docs_file_id).first()
    if not doc:
        raise NoResultFound(f" No Design Document found for this project ID {design_docs_file_id}")
    
    db.delete(doc)    
    db.commit()
    
