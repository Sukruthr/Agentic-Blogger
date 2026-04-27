import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


class GroqLLLM:
    def __init__(self) -> None:
        load_dotenv()
        os.environ["GROQ_API_KEY"]=self.groq_api_key= os.getenv("GROQ_API_KEY")

    def get_llm(self):
        try:
            llm=ChatGroq(api_key=self.groq_api_key, model="qwen/qwen3-32b")
            return llm
        except Exception as e:
            return ValueError f"error occured with expcetion {e}"
