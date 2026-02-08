from langchain_community.document_loaders import PyPDFLoader , TextLoader 


class DataLoader:
    def __init__(self, file_path: str):
        self.path = file_path

    def _check_file_type(self):
        return self.path.split(".")[-1].lower()

    def load(self):
        ext = self._check_file_type()

        if ext == "pdf":
            loader = PyPDFLoader(self.path)
        elif ext == "txt":
            loader = TextLoader(self.path, encoding="utf-8")
        else:
            raise ValueError(f"Unsupported file type: {ext}")

        return loader.load()
