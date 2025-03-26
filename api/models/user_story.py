from sqlalchemy import Column, String, Integer, ForeignKey, Enum as SQLEnum, Text, ARRAY
from sqlalchemy.dialects.postgresql import UUID
import uuid
from enum import Enum
from database import Base


class PriorityEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class UserStory(Base):
    __tablename__ = "user_stories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    acceptance_criteria = Column(Text, nullable=False)  
    priority = Column(SQLEnum(PriorityEnum), nullable=False)
    storyPoints = Column(Integer, nullable=False)
    labels = Column(ARRAY(String), nullable=True)  
    issueType = Column(Text, nullable=False)
