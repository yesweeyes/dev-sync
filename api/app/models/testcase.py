from database import Base
from sqlalchemy import Column, String, ForeignKey, Enum as SQLEnum, Text, ARRAY, TIMESTAMP, text, Boolean, Integer
import uuid
from sqlalchemy.dialects.postgresql import UUID
from enum import Enum

class TestCasePriorityEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class TestCase(Base):
    __tablename__ = "test_case"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, primary_key=True)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id", ondelete="CASCADE"), nullable=False)
    module_name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    preconditions = Column(Text, nullable=False)
    test_steps = Column(ARRAY(Text), nullable=False)
    post_condition = Column(Text, nullable=False)
    priority = Column(SQLEnum(TestCasePriorityEnum), nullable=False)
    test_type =Column(String, nullable=False)
    jiraPush = Column(Boolean, default=False)
    jira_id = Column(Integer, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
