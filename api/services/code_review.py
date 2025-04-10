from typing import List
import uuid
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models.code_review import CodeReviewFile
from schemas.code_review import CodeReviewBase, CodeReviewCreate, CodeReviewUpdate
from services.project import get_project as get_project_service
from utils.code_review.parse_repo import (
    clone_github_repo as clone_github_repo_util,
    read_code_from_temp_dir as read_code_from_temp_dir_util,
)
from utils.code_review.generate_review_file import (
    generate_code_review_html as generate_code_review_html_util
)
from utils.code_review.save_review_to_file import (
    save_review_to_file as save_review_to_file_util
)

def save_code_review_file(db: Session, project_id: uuid.UUID, file_name: str, file_path: str) -> CodeReviewFile:
    unique_filename = f"{uuid.uuid4()}_{file_name}"

    code_review_file = CodeReviewFile(
        project_id=project_id,
        original_name=file_name,
        stored_name=unique_filename,
        file_path=file_path,
    )

    db.add(code_review_file)
    db.commit()
    db.refresh(code_review_file)

    return code_review_file

def get_code_review_file_by_id(db: Session, doc_id: uuid.UUID) -> CodeReviewFile:
    doc = db.query(CodeReviewFile).filter(CodeReviewFile.id == doc_id).first()
    if not doc:
        raise NoResultFound(f"Requirement Document with ID {doc_id} not found")
    return doc

def update_code_review_file(db: Session, code_review_file_data: CodeReviewUpdate) -> CodeReviewFile:
    code_review = db.query(CodeReviewFile).filter(CodeReviewFile.id == code_review_file_data.id).first()
    if not code_review:
        raise NoResultFound(f"Code Review file with ID {code_review_file_data.id} not found")

    for key, value in code_review_file_data.model_dump(exclude_unset=True).items():
        setattr(code_review, key, value)

    db.commit()
    db.refresh(code_review)
    return code_review

def delete_code_review_file(db: Session, code_review_id: uuid.UUID):
    code_review = db.query(CodeReviewFile).filter(CodeReviewFile.id == code_review_id).first()
    if not code_review:
        raise NoResultFound(f"Code Review file with ID {code_review_id} not found")

    db.delete(code_review)
    db.commit()

def get_all_code_review_file_for_project(db: Session, project_id: uuid.UUID) -> List[CodeReviewFile]:
    return db.query(CodeReviewFile).filter(CodeReviewFile.project_id == project_id).all()

def generate_code_review_file(db: Session, project_id: uuid.UUID, user_prompt: str):
    project = get_project_service(db, project_id)
    github_endpoint = project.github_endpoint

    temp_dir = clone_github_repo_util(github_endpoint=github_endpoint)
    code = read_code_from_temp_dir_util(temp_dir)
    html_string = generate_code_review_html_util(code, user_prompt=user_prompt)
    file_path, file_name = save_review_to_file_util(html_string)
    code_review_file = save_code_review_file(db, project_id, file_name, file_path)

    return code_review_file
