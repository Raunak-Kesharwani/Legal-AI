from langchain_classic.chains.summarize import load_summarize_chain


class Summarizer:
    
    def __init__(self , model , text):
        self.model = model 
        self.text = text

    def summarize(self):
        return load_summarize_chain(self.model,
                                     chain_type="map_reduce").invoke(self.text)