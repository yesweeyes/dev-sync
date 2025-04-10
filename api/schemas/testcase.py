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

    class Config:
        from_attributes = True 

class TestCaseUpdate(BaseModel):
    module_name: Optional[str]
    description: Optional[str]
    preconditions: Optional[str]
    test_steps : Optional[List[str]]
    post_condition: Optional[str]
    priority: Optional[PriorityEnum]
    test_type: Optional[str]

    class Config:
        from_attributes = True 
