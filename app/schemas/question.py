from typing import List

from pydantic import BaseModel

class Requestquestion(BaseModel):
    request : str

class Responsequestion(BaseModel):
    answer : str

# 질문(농작물)과 관련된 사이트를 추천해주는 스키마
# class ResponseURL(BaseModel): 
#    answer : str