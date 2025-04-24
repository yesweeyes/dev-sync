import os
import uuid
import traceback
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.design_document import GeneratedHLDDocument,GeneratedLLDDocument
from app.schemas.design_doc import HldLldGenerate
from app.utils.design_doc.llm_processor import process_with_llm
import app.utils.user_story.generate_user_stories as user_story_gen_util
from app.services.design_doc import delete_design_documents as delete_design_documents_file_service
from app.services.document_summary import get_document_summary_by_project

router = APIRouter(
    prefix="/tech_docs",
    tags=["tech_docs"],
)

@router.post("/generate")
def GenerateDesignDocs(data:HldLldGenerate, db: Session =Depends(get_db)):
    project_id=data.project_id
               
    # processing of summary with LLM
    summary=get_document_summary_by_project(project_id)    
    hld_pdf, lld_pdf = process_with_llm(summary)

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

@router.delete("/{design_docs_file_id}")
def delete_design_docs(design_docs_file_id: uuid.UUID, db:Session = Depends(get_db)):
    try: 
        delete_design_documents_file_service(db,design_docs_file_id)
        return {"detail": "Design Docs Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
