import os

from langchain.chat_models import ChatOpenAI
# from openai import AzureOpenAI > 가장 최근 나온 버전으로 바꿀 것..
from core.config import settings
from question.prompts import prompt_templates

class Question:
    def __init__(self):
        # OpenAI API 초기화
        self.llm = ChatOpenAI(
            model_name="gpt-4", # or 'gpt-3.5-turbo', 'gpt-4o'
            temperature=0,
            openai_api_key=settings.OPENAI_API_KEY,
        )

        # Azure OpenAI 사용 시        
        # self.llm2 = AzureOpenAI(
        #    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        #    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        #    api_version="2024-02-01-preview"
        # )
    
    def run(self, question: str) -> dict:
        # 원문 답변 프롬프트 생성
        question_prompt = prompt_templates["question"].format(answer=question)
        english_answer = self.llm.predict(question_prompt)

        # 번역 프롬프트 생성
        translation_prompt = prompt_templates["translation"].format(answer=english_answer)
        translated_answer = self.llm.predict(translation_prompt)

        return translated_answer

        