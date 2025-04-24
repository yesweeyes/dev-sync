from pydantic import BaseModel, UUID4, ConfigDict

class HldLldBase(BaseModel):
    id: UUID4
    project_id: UUID4
    original_name: str
    stored_name: str
    file_path: str

    model_config = ConfigDict(from_attributes=True)

class HldLldGenerate(BaseModel):
    project_id: UUID4

    model_config = ConfigDict(from_attributes=True)

