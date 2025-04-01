from pydantic import BaseModel, UUID4, Field
from typing import List, Optional
from enum import Enum

class PriorityEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class UserStoryBase(BaseModel):
    project_id : UUID4
    title: str
    description: str
    acceptance_criteria: str
    priority : PriorityEnum
    storyPoints: int = Field(..., gt=0)
    labels : List[str]
    issueType: str

    class Config:
        from_attributes = True 

class CreateUserStory(UserStoryBase):
    pass

class UpdateUserStory(UserStoryBase):
    title: Optional[str]
    description: Optional[str]
    acceptance_criteria: Optional[List[str]]
    priority : Optional[PriorityEnum]
    storyPoints: Optional[int] = Field(None, gt=0)
    labels : Optional[List[str]]
    issueType : Optional[str]

    class Config:
        from_attributes = True 

