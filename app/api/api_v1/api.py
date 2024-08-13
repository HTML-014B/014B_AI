from fastapi import APIRouter

from api.api_v1.endpoints import question_v1, question_v2

api_router = APIRouter()
api_router.include_router(question_v1.router, prefix="/question", tags=["questions"])

# api_router.include_router(question_v2.router, prefix="/question", tags=["questions"])