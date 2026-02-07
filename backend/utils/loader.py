from langchain_community.document_loaders import PyPDFLoader , TextLoader 


class DataLoader:
    def __init__(self, file_path: str):
        self.path = file_path

    def _check_file_type(self):
        return self.path.split(".")[-1].lower()

    def load(self):
        ext = self._check_file_type()

        try:
            if ext == "pdf":
                loader = PyPDFLoader(self.path)
            elif ext == "txt":
                loader = TextLoader(self.path, encoding="utf-8")
            else:
                raise ValueError(f"Unsupported file type: {ext}")

            pages = [doc for doc in loader.lazy_load()]

            return pages if len(pages) <= 10 else []

        except Exception as e:
            raise RuntimeError(f"Failed to load file: {e}") from e
