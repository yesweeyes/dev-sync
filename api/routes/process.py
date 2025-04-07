from sqlalchemy.orm import Session
from database import get_db
from models.db_models import Generated_HLD_Document,Generated_LLD_Document

import os
from fastapi import APIRouter, UploadFile, File, Depends, Query, HTTPException
from utils.Tech_Docs.extractor import extract_text_from_pdf, save_to_docx
from utils.Tech_Docs.llm_processor import process_with_llm
import uuid

UPLOAD_DIR = "uploads/tech_docs"
OUTPUT_DIR = "outputs"

router = APIRouter(
    prefix="/tech_docs",
    tags=["tech_docs"],
)

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...), project_id: uuid.UUID =Query(...), db: Session =Depends(get_db)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    # extracting text and saving as a docx
    text_chunks = extract_text_from_pdf(file_path)
    docx_path = os.path.join(OUTPUT_DIR, "extracted_docx.docx")
    save_to_docx(text_chunks, docx_path)

    # processing of extracted text with LLM
    hld_pdf, lld_pdf = process_with_llm(docx_path)

    try:

        #for HLD
        new_hld=Generated_HLD_Document(
            project_id=project_id,
            original_name="HLD_Document.pdf",
            stored_name=os.path.basename(hld_pdf),
            file_path=hld_pdf
        
        )

        #for LLD
        new_lld=Generated_LLD_Document(
            project_id=project_id,
            original_name="LLD_Document.pdf",
            stored_name=os.path.basename(lld_pdf),
            file_path=lld_pdf
            
        )
        db.add(new_hld)
        db.add(new_lld)

        db.commit()
        db.refresh(new_hld)
        db.refresh(new_lld)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    

    return {"updates": "Processing complete", "HLD_PDF": hld_pdf, "LLD_PDF": lld_pdf}
