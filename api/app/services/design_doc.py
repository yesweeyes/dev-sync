import uuid
from typing import List, Union
from sqlalchemy.orm import Session
from app.models.tech_db import GeneratedHLDDocument,GeneratedLLDDocument


def get_all_design_documents(db:Session, project_id:uuid.UUID) -> List[Union[GeneratedHLDDocument,GeneratedLLDDocument]]:
    hld_document=db.query(GeneratedHLDDocument).filter(GeneratedHLDDocument.project_id == project_id).all()
    lld_document=db.query(GeneratedLLDDocument).filter(GeneratedLLDDocument.project_id == project_id).all()

    return hld_document+lld_document
