from pydantic import BaseModel, UUID4, ConfigDict
from typing import Optional
from datetime import datetime

class RequirementDocumentBase(BaseModel):
    id: UUID4
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class RequirementDocumentCreate(BaseModel):
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str

    model_config = ConfigDict(from_attributes=True)

class RequirementDocumentUpdate(BaseModel):
    original_name: Optional[str] = None
    stored_name: Optional[str] = None
    file_path: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
