from pydantic import BaseModel
from sqlmodel import Field, SQLModel

class Project(BaseModel):
    name: str
    description: str | None = None

