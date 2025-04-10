from pydantic import BaseModel, UUID4
from typing import Optional

class JiraIssueBase(BaseModel):
    project_id:UUID4
    issue_id:int
    key: str
    end_point : str
    issue_type:str
    parent_id:UUID4

class JiraIssueCreate(BaseModel):
    id:UUID4
    project_id:UUID4
    issue_id:int
    key: str
    end_point : str
    issue_type:str
    parent_id:UUID4



