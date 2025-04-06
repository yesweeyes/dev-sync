from database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, String
import uuid

class JiraIssues(Base):
    __tablename__ = "jira_issues"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id", ondelete="CASCADE"), nullable=False)
    issue_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    key = Column(String, nullable=False)
    end_point = Column(String, nullable=False)

    class Config:
        from_attributes = True