from fastapi import APIRouter

from api.api_v1.endpoints import question

api_router = APIRouter()
api_router.include_router(question.router, prefix="/question", tags=["questions"])