import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/uploads",
    tags=["uploads"],
)

@router.get("/{filename}")
def serve_file(filename: str):
    file_path = os.path.join("uploads", filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type='application/pdf')
    raise HTTPException(status_code=404, detail="File not found")

