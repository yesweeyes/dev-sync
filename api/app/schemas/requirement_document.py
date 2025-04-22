from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

class RequirementDocumentBase(BaseModel):
    id: UUID4
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str
    created_at: datetime

    class Config:
        from_attributes = True

class RequirementDocumentCreate(BaseModel):
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str

    class Config:
        from_attributes = True

class RequirementDocumentUpdate(BaseModel):
    original_name: Optional[str] = None
    stored_name: Optional[str] = None
    file_path: Optional[str] = None

    class Config:
        from_attributes = True
