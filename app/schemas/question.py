from typing import List

from pydantic import BaseModel

class Requestquestion(BaseModel):
    request : str

class Responsequestion(BaseModel):
    answer : str

class ResponseURL(BaseModel):
    answer : str