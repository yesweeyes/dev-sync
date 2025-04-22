from typing import List, Union
import uuid
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models.tech_db import GeneratedHLDDocument,GeneratedLLDDocument
from schemas.design_doc import HldLldBase, HldLldGenerate
from fastapi.responses import FileResponse
import os


def get_all_design_documents(db:Session, project_id:uuid.UUID) -> List[Union[GeneratedHLDDocument,GeneratedLLDDocument]]:
    hld_document=db.query(GeneratedHLDDocument).filter(GeneratedHLDDocument.project_id == project_id).all()
    lld_document=db.query(GeneratedLLDDocument).filter(GeneratedLLDDocument.project_id == project_id).all()

    return hld_document+lld_document
