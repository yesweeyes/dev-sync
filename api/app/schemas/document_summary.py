from pydantic import BaseModel, UUID4
from datetime import datetime

class DocumentSummaryBase(BaseModel):
    id: UUID4
    project_id: UUID4
    document_id: UUID4
    summary: str
    created_at: datetime

class DocumentSummaryCreate(BaseModel):
    project_id: UUID4
    document_id: UUID4
    summary: str