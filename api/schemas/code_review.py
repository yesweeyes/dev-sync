from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class CodeReviewBase(BaseModel):
    id: UUID4
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str
    created_at: datetime

    class Config:
        from_attributes = True

class CodeReviewCreate(BaseModel):
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str

    class Config:
        from_attributes = True

class CodeReviewUpdate(BaseModel):
    original_name: Optional[str] = None

    class Config:
        from_attributes = True

class CodeReviewGenerate(BaseModel):
    project_id: UUID4
    user_prompt: str