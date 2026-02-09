from backend.utils.chunker import TextSplitter

class LegalChat:
    def __init__(self,model,text):
        self.base_model = model
        self.text = text

    def embeddings(self):
        chunks = TextSplitter(self.text).embed_split()
        
        vectors = self.base_model.embed_documents(chunks)
        
        return vectors