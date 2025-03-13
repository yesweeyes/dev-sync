from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.services.healthcheck_llm import HealthCheckLLMService

router = APIRouter(
    prefix="/healthcheck-llm",
    tags=["healthcheck_llm"],
)

service = HealthCheckLLMService()

@router.get("/")
async def healthcheck_llm():
    result = service.healthcheck_llm()
    
    if result is None:
        return JSONResponse(status_code=500)
    
    return JSONResponse(
        status_code=200,
        content=result
    )
