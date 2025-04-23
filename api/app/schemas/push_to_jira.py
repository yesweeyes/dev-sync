from pydantic import BaseModel
from enum import Enum

class JiraIssueTypeEnum(str, Enum):
    BUG = "Bug"
    STORY = "Story"
    TASK = "Task"

    

class PushToJiraData(BaseModel):
    summary: str
    description: str
    issueType: JiraIssueTypeEnum