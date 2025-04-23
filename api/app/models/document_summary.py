import uuid
from sqlalchemy import Column, ForeignKey, Enum as SQLEnum, Text, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class DocumentSummary(Base):
    __tablename__ = "document_summary"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id", ondelete="CASCADE"), nullable=False)
    document_id = Column(UUID(as_uuid=True), ForeignKey("requirement_document.id", ondelete="CASCADE"), nullable=False)
    summary = Column(Text, nullable=False, default=text(''))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))