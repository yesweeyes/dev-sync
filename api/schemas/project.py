from pydantic import BaseModel, UUID4, EmailStr
from typing import Optional

class ProjectSchema(BaseModel):
    name: str
    jira_project_key: str
    jira_project_auth: str
    jira_project_endpoint: str
    jira_project_email: EmailStr  # Ensures valid email format

    class Config:
        from_attributes = True  # Allows conversion from ORM model
