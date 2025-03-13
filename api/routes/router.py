from fastapi import APIRouter
from api.routes.project import router as project_router
from api.routes.requirement_document import router as requirement_document_router

router = APIRouter(prefix="/api", tags=["api"])

router.include_router(project_router)
router.include_router(requirement_document_router)