from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextSplitter:
    def __init__(self,Text):
        self.text = Text 

    def _splitter(self , chunk_size , chunk_overlap ):
        chunker = RecursiveCharacterTextSplitter(chunk_size = chunk_size , chunk_overlap=chunk_overlap)
        return chunker.split_documents(self.text) 

    def for_embedding(self):
        return self._splitter(chunk_size = 250 , chunk_overlap = 0)

    def for_summary(self):
        return self._splitter(chunk_size = 1000, chunk_overlap = 100)
