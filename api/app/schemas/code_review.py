from pydantic import BaseModel, UUID4, ConfigDict
from datetime import datetime
from typing import Optional

class CodeReviewBase(BaseModel):
    id: UUID4
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CodeReviewCreate(BaseModel):
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str

    model_config = ConfigDict(from_attributes=True)

class CodeReviewUpdate(BaseModel):
    original_name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class CodeReviewGenerate(BaseModel):
    project_id: UUID4
    user_prompt: str