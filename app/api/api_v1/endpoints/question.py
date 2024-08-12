from typing import Any
import logging

from fastapi import APIRouter, HTTPException

from question.question import Question
from schemas.question import Requestquestion, Responsequestion
# from app.utils import PreProcessor, parsing_generation_output
# from app.utils.decorators import live_mode, validate_content

router = APIRouter()
question = Question()
logger = logging.getLogger(__name__)

@router.post("/request", response_model= Responsequestion)
async def request_question(req: Requestquestion) -> Responsequestion:
    """
    Generate a response that includes a summary and answer from a question.\n
    A question (string) is required in the request body.
    """
    
    try: 
        result = question.run(req.request)
        return Responsequestion(answer=result)
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")