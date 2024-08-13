# from typing import Any
import logging 

from fastapi import APIRouter, HTTPException

from question.question2 import Question
from schemas.question import Requestquestion, Responsequestion

router = APIRouter()
question = Question()
logger = logging.getLogger(__name__)

@router.post("/new_request", response_model= Responsequestion)
async def request_question(req: Requestquestion) -> Responsequestion:
    """
    Generate a response that includes a summary and answer from a question.\n
    A question (string) is required in the request body.
    """
    try:
        # run2 메서드 호출
        result = question.run2(req.request)
        
        # `completion` 객체에서 실제 답변 추출
        answer = result.choices[0].message['content'] if result.choices else "No answer generated."
        
        return Responsequestion(answer=answer)
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")