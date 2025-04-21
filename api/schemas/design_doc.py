from pydantic import BaseModel, UUID4

class HldLldBase(BaseModel):
    id: UUID4
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str

    class Config:
        from_attributes=True

class HldLldGenerate(BaseModel):
    project_id: UUID4

    class Config:
        from_attributes=True

