from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

class LLDTechBase(BaseModel):
    id: UUID4
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str
    created_at: datetime

    class Config:
        from_attributes = True

class LLDTechCreate(BaseModel):
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str

    class Config:
        from_attributes = True

class LLDTechUpdate(BaseModel):
    original_name: Optional[str] = None
    

    class Config:
        from_attributes = True
