from fastapi import APIRouter
from .project import router as project_router
from .requirement_document import router as requirement_document_router
from .healthcheck_llm import router as health_check_llm_router

router = APIRouter(prefix="/api", tags=["api"])

router.include_router(project_router)
router.include_router(requirement_document_router)
router.include_router(health_check_llm_router)