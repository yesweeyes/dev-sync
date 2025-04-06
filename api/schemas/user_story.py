from pydantic import BaseModel, UUID4, Field
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

    class Config:
        from_attributes = True 

class UserStoryCreate(BaseModel):
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

class UserStoryUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    acceptance_criteria: Optional[Union[str, List[str]]]
    priority : Optional[PriorityEnum]
    storyPoints: Optional[int] = Field(None, gt=0)
    labels : Optional[List[str]]
    issueType : Optional[str]

    class Config:
        from_attributes = True 

class UserStoryGenerate(BaseModel):
    project_id: UUID4
    user_prompt: str

