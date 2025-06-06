import uuid
from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class Project(Base):
    __tablename__ = "project"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    jira_project_key = Column(String, nullable=False)
    jira_project_auth = Column(String, nullable=False)
    jira_project_endpoint = Column(String, nullable=False)
    jira_project_email = Column(String, nullable=False)
    github_endpoint = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))