from langchain_google_genai import ChatGoogleGenerativeAI , GoogleGenerativeAIEmbeddings

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

class EmbedModel:
    def __init__(self , api_key : str):
        self.api = api_key

    def get_model(self):
        return GoogleGenerativeAIEmbeddings(
            model = "gemini-embedding-001",
            api_key=self.api,
            output_dimensionality=512
        )