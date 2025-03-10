import os
from langchain_community.chat_models import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

class OpenAIReviewer:
    def __init__(self, model_name="gpt-4"):
        self.llm = ChatOpenAI(model_name=model_name, temperature=0.3)

    def analyze_code(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            code_content = file.read()

        messages = [
            SystemMessage(content="You are a code review assistant. Analyze the given code and provide feedback."),
            HumanMessage(content=f"Review the following code:\n\n{code_content}")
        ]

        response = self.llm(messages)
        return response.content

class OllamaReviewer:
    def __init__(self, model_name="llama3"):
        self.llm = OllamaLLM(model=model_name)

    def analyze_code(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            code_content = file.read()

        messages = [
            SystemMessage(content="You are a code review assistant. Analyze the given code and provide feedback."),
            HumanMessage(content=f"Review the following code:{code_content}")
        ]

        response = self.llm.invoke(messages)
        return response

def get_code_reviewer():
    use_ollama = os.getenv("OLLAMA_MODEL")
    if use_ollama:
        return OllamaReviewer(model_name=use_ollama)
    return OpenAIReviewer(model_name=os.getenv("MODEL_NAME", "gpt-4"))