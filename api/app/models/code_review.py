from database import Base
from sqlalchemy import TIMESTAMP, Column, String, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
import uuid

class CodeReviewFile(Base):
    __tablename__ = "code_review_file"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id", ondelete="CASCADE"), nullable=False)
    original_name = Column(String, nullable=False)
    stored_name = Column(String, nullable=False)  
    file_path = Column(String, nullable=False)      
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
