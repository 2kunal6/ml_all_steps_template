import chromadb

class ChromaDB:
    chroma_client = None
    def __init__(self):
        self.chroma_client = chromadb.Client()
        self.collection = self.chroma_client.create_collection(name="my_collection")
        self.collection.add(documents=["This is a document", "This is another document"], ids=["id1", "id2"])

    def get_inference(self, k):
        return self.collection.query(query_texts=[k], n_results=2)
