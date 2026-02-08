from langchain_google_genai import ChatGoogleGenerativeAI

class ChatModel:
    def __init__(self, api_key: str):
        self.api = api_key

    def get_model(self):
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",  
            google_api_key=self.api,
            temperature=0.4,
            max_tokens=2000
        )
