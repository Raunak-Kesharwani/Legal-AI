from langchain_google_genai import ChatGoogleGenerativeAI

class ChatModel:

    def __init__(self , api_key):
        self.api = api_key     
        
    def chatmodel(self):
        model = ChatGoogleGenerativeAI(
            model = "gemini-2.5-flash-lite",
            google_api_key = self.api,
            max_tokens = 1000,
            temperature = 0.5
        )
        return model 