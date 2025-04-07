from fastapi import APIRouter
from .project import router as project_router
from .requirement_document import router as requirement_document_router
from .user_story import router as user_story_router
from .process import router as tech_router

router = APIRouter(prefix="/api/v1", tags=["api"])

router.include_router(project_router)
router.include_router(requirement_document_router)
router.include_router(user_story_router)
router.include_router(tech_router)