from pydantic import BaseModel, UUID4, Field
from typing import Optional, List
from enum import Enum

class PriorityEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class TestCaseBase(BaseModel):
    id:UUID4
    project_id:UUID4
    module_name:str
    title:str
    description: str
    preconditions: str
    test_steps : List[str]
    post_condition: str
    priority:PriorityEnum
    test_type:str
    jiraPush:bool
    jira_id:int

    class Config:
        from_attributes = True 

class TestCaseCreate(BaseModel):
    project_id:UUID4
    module_name:str
    title:str
    description: str
    preconditions: str
    test_steps : List[str]
    post_condition: str
    priority:PriorityEnum
    test_type:str
    jiraPush:Optional[bool] = None
    jira_id:Optional[int] = None

    class Config:
        from_attributes = True 

class TestCaseUpdate(BaseModel):
    module_name: Optional[str] = None
    description: Optional[str] = None
    preconditions: Optional[str] = None
    test_steps : Optional[List[str]] = None
    post_condition: Optional[str] = None
    priority: Optional[PriorityEnum] = None
    test_type: Optional[str] = None
    jiraPush:Optional[bool] = None
    jira_id:Optional[int] = None

    class Config:
        from_attributes = True 
