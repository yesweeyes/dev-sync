import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/tech_docs",
    tags=["tech_docs"],
)

@router.get("/{filename}")
def serve_lld_file(filename: str):
    file_path = os.path.join("app","local_fs","lowlevel_doc",filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='application/pdf')
    raise HTTPException(status_code=404, detail="File not found")