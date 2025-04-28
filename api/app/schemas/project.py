from pydantic import BaseModel, UUID4, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

class ProjectCreate(BaseModel):
    name: str
    jira_project_key: str
    jira_project_auth: str
    jira_project_endpoint: str
    jira_project_email: EmailStr
    github_endpoint: str

class ProjectBase(BaseModel):
    id: UUID4
    name: str
    jira_project_key: str
    jira_project_auth: str
    jira_project_endpoint: str
    jira_project_email: EmailStr
    github_endpoint: str
    created_at: datetime

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    jira_project_key: Optional[str] = None
    jira_project_auth: Optional[str] = None
    jira_project_endpoint: Optional[str] = None
    jira_project_email: Optional[EmailStr] = None
    github_endpoint: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
