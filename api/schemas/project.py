from pydantic import BaseModel, UUID4, EmailStr
from typing import Optional

class ProjectBase(BaseModel):
    name: str
    jira_project_key: str
    jira_project_auth: str
    jira_project_endpoint: str
    jira_project_email: EmailStr

class ProjectCreate(ProjectBase):
    id: Optional[UUID4] = None  

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    jira_project_key: Optional[str] = None
    jira_project_auth: Optional[str] = None
    jira_project_endpoint: Optional[str] = None
    jira_project_email: Optional[EmailStr] = None

    class Config:
        from_attributes = True
