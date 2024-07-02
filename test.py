import os
from langchain.llms import HuggingFaceEndpoint

api_key = os.getenv("huggingfacehub_api_token")
llm=HuggingFaceEndpoint(
        huggingfacehub_api_token=api_key, 
        repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1", 
        temperature = 0.8,
        max_length = 150
        )
llm.invoke("What is data science")