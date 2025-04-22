from sqlalchemy.orm import Session
from database import get_db
from models.tech_db import GeneratedHLDDocument,GeneratedLLDDocument
from schemas.design_doc import HldLldGenerate

import os
from fastapi import APIRouter, Depends, HTTPException
from utils.design_doc.extractor import extract_text_from_pdf, save_to_docx
from utils.design_doc.llm_processor import process_with_llm
import utils.user_story.generate_user_stories as user_story_gen_util
import traceback

output_dir = "output"

router = APIRouter(
    prefix="/tech_docs",
    tags=["tech_docs"],
)

os.makedirs(output_dir, exist_ok=True)

@router.post("/generate/")
def GenerateDesignDocs(data:HldLldGenerate, db: Session =Depends(get_db)):
    project_id=data.project_id
    
    document=user_story_gen_util.get_files(project_id,db)
       
    # extracting text and saving as a docx
    text_chunks = extract_text_from_pdf(document)
    #docx_path = os.path.join(output_dir, "extracted_docx.docx")
    #save_to_docx(text_chunks, docx_path)

    # processing of extracted text with LLM
    hld_pdf, lld_pdf = process_with_llm(text_chunks)

    try:

        #for HLD
        new_hld=GeneratedHLDDocument(
            project_id=project_id,
            original_name="HLD_Document.pdf",
            stored_name=os.path.basename(hld_pdf),
            file_path=hld_pdf
        
        )

        #for LLD
        new_lld=GeneratedLLDDocument(
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
        print("Error Occured: ",str(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error....~.")
    
    return {"updates": "Processing complete", "HLD_PDF": hld_pdf, "LLD_PDF": lld_pdf}
