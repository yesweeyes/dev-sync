from pydantic import BaseModel, UUID4
from typing import Optional

class JiraIssueBase(BaseModel):
    project_id:UUID4
    issue_id:int
    key: str
    end_point : str

class CreateJiraIssue(JiraIssueBase):
    pass

class UpdateJiraIssue(JiraIssueBase):
    project_id: Optional[UUID4] = None
    issue_id: Optional[int] = None
    key: Optional[str] = None
    end_point: Optional[str] = None

