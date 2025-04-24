from pydantic import BaseModel, UUID4, Field, ConfigDict
from typing import List, Optional, Union
from enum import Enum

class PriorityEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class UserStoryBase(BaseModel):
    id: UUID4
    project_id : UUID4
    title: str
    description: str
    acceptance_criteria: str
    priority : PriorityEnum
    storyPoints: int = Field(..., gt=0)
    labels : List[str]
    issueType: str
    jira_id:int
    jiraPush : bool

    model_config = ConfigDict(from_attributes=True)

class UserStoryCreate(BaseModel):
    project_id : UUID4
    title: str
    description: Optional[str] = None
    acceptance_criteria: Optional[str] = None
    priority : Optional[PriorityEnum] = None
    storyPoints: Optional[int] = None
    labels : Optional[List[str]] = None
    issueType: str
    jiraPush : bool
    jira_id:int

    model_config = ConfigDict(from_attributes=True)

class UserStoryUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    acceptance_criteria: Optional[Union[str, List[str]]] = None
    priority : Optional[PriorityEnum] = None
    storyPoints: Optional[int] = Field(None, gt=0)
    labels : Optional[List[str]] = None
    issueType : Optional[str] = None
    jiraPush:Optional[bool] = None
    jira_id : Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

class UserStoryGenerate(BaseModel):
    project_id: UUID4
    user_prompt: str

