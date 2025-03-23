from pydantic import BaseModel
from typing import TypedDict, Any, Dict

class Document(BaseModel):
    content: str
    metadata: Dict[str, Any]  
    id: str

class AddDocumentRequestData(BaseModel):
    project_id: str
    document: Document
    collection_name: str = "db"

class QueryDocumentRequestData(BaseModel):
    project_id: str
    query_text: str = None
    top_k: int  = 5
    collection_name: str = "db"