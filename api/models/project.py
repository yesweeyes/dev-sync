from pydantic import BaseModel

class Project(BaseModel):
    name: str
    description: str | None = None

