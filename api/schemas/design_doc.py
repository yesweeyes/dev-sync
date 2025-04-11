from pydantic import BaseModel, UUID4

class HldLldGenerate(BaseModel):
    project_id: UUID4

    class Config:
        from_attributes=True

