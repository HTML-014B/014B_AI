# import os
# from openai import AzureOpenAI # > 가장 최근 나온 버전으로 바꿀 것..
# from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# class Question:
#     def __init__(self):

#         self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "https://joonhyuk-lee.openai.azure.com/")
#         self.deployment = os.getenv("AZURE_DEPLOYMENT_NAME", "FARMIN-gpt")
#         self.token_provider = get_bearer_token_provider(
#             DefaultAzureCredential(),
#             "https://cognitiveservices.azure.com/.default"
#         )
    
#     def run2(self, question: str) -> dict:
#          # 답변 프롬프트 생성
#         self.client = AzureOpenAI(
#             azure_endpoint = self.endpoint,
#             azure_deployment = self.deployment,
#             azure_ad_token_provider = self.token_provider,
#             api_version="2024-05-01-preview"
#         )
        
#         completion = self.client.chat.completions.create(
#             model = self.deployment,
#             messages= [
#             {
#                 "role": "user",
#                 "content": question
#             }],
#             max_tokens=800,
#             temperature=0.7,
#             top_p=0.95,
#             frequency_penalty=0,
#             presence_penalty=0,
#             stop=None,
#             stream=False
#         )
#         return completion