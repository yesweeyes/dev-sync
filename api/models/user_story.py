from sqlalchemy import Column, String, Integer,Boolean, ForeignKey, Enum as SQLEnum, Text, ARRAY, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
import uuid
from enum import Enum
from database import Base


class UserStoryPriorityEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class UserStory(Base):
    __tablename__ = "user_story"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    acceptance_criteria = Column(Text)  
    priority = Column(SQLEnum(UserStoryPriorityEnum))
    storyPoints = Column(Integer)
    labels = Column(ARRAY(String))  
    issueType = Column(Text, nullable=False)
    jiraPush = Column(Boolean, default=False)
    jira_id = Column(Integer, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
