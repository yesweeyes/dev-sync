import os
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
)

@router.get("/{filename}")
def serve_file(filename: str):
    file_path = os.path.join("reviews", filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    # Determine media type based on file extension
    ext = os.path.splitext(filename)[1].lower()
    media_types = {
        '.html': 'text/html',
        '.htm': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.json': 'application/json',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.svg': 'image/svg+xml',
    }
    media_type = media_types.get(ext, 'application/octet-stream')

    return FileResponse(file_path, media_type=media_type)