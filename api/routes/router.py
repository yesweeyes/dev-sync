from fastapi import APIRouter
from .project import router as project_router
from .requirement_document import router as requirement_document_router
from .user_story import router as user_story_router
from .testcases import router as test_case_router
from .design_doc import router as tech_router
from .code_review import router as code_review_router
from .uploads import router as upload_router
from .reviews import router as review_router

router = APIRouter(prefix="/api/v1", tags=["api"])

router.include_router(project_router)
router.include_router(requirement_document_router)
router.include_router(user_story_router)
router.include_router(test_case_router)
router.include_router(tech_router)
router.include_router(code_review_router)
router.include_router(upload_router)
router.include_router(review_router)
