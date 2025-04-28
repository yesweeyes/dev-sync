from fastapi import APIRouter
from app.routes.project import router as project_router
from app.routes.requirement_document import router as requirement_document_router
from app.routes.user_story import router as user_story_router
from app.routes.testcases import router as test_case_router
from app.routes.design_doc import router as tech_router
from app.routes.code_review import router as code_review_router
from app.routes.uploads import router as upload_router
from app.routes.reviews import router as review_router
from app.routes.highlevel_doc import router as hld_router
from app.routes.lowlevel_doc import router as lld_router

router = APIRouter(prefix="/api/v1", tags=["api"])

router.include_router(project_router)
router.include_router(requirement_document_router)
router.include_router(user_story_router)
router.include_router(test_case_router)
router.include_router(tech_router)
router.include_router(code_review_router)
router.include_router(upload_router)
router.include_router(review_router)
router.include_router(hld_router)
router.include_router(lld_router)
