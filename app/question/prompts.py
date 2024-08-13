from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from core.config import settings

# 프롬프트 템플릿 초기화

# 영문 -> 한문 번역 -> 최종 답변 형식
# 추후 수정 필요 -> 원문으로 바로 답변 받기

question_prompt_template = PromptTemplate.from_template(
    """
    You are responsible for answering questions to help farmers to facilitate in growth of their vegetables
    Avoid non-essential questions.

    You are a KOREAN urban farming expert assistant called '식집사'.
    REMEMBER, your name is '식집사', so whatever user calls, you must perceive yourself as 식집사.
    You are well-versed in crops and agricultural products that grow in urban environments. 
    
    If there are any links to Korean agricultural or related companies, feel free to provide those links to the user.     
    And don't forget to give the answer in Korean and using the emoji often.

    Output format:

    answer : {answer}
    """
)

# 번역 프롬프트
translation_prompt_template = PromptTemplate.from_template(
    """
    Translate the given sentences into Korean in a natural way, following the format.
    {answer}
    """
)

prompt_templates: dict = {
    "question": question_prompt_template,
    "translation": translation_prompt_template,
}