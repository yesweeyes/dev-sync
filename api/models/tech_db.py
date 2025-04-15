from database import Base
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid

class GeneratedHLDDocument(Base):

    __tablename__ = "hld_document"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id", ondelete="CASCADE"), nullable=False, unique=True)
    original_name = Column(String, nullable=False)
    stored_name = Column(String, nullable=False)  
    file_path = Column(String, nullable=False)

class GeneratedLLDDocument(Base):
     
     __tablename__ = "lld_document"
     id=Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
     project_id = Column(UUID(as_uuid=True), ForeignKey("project.id", ondelete="CASCADE"), nullable=False, unique=True)
     original_name = Column(String, nullable=False)
     stored_name = Column(String, nullable=False)  
     file_path = Column(String, nullable=False)
