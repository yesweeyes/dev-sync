from pydantic import BaseModel, UUID4
from typing import Optional

class RequirementDocumentBase(BaseModel):
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str

class RequirementDocumentCreate(RequirementDocumentBase):
    pass

class RequirementDocumentUpdate(BaseModel):
    original_name: Optional[str] = None
    stored_name: Optional[str] = None
    file_path: Optional[str] = None

    class Config:
        from_attributes = True
