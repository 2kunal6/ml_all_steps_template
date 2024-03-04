import chromadb

class ChromaDB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.chroma_client = chromadb.Client()
            cls.collection = cls.chroma_client.create_collection(name="my_collection")
            cls.collection.add(documents=["This is a document", "This is another document"], ids=["id1", "id2"])
        return cls._instance

    def get_inference(self, k):
        return self.collection.query(query_texts=[k], n_results=2)
