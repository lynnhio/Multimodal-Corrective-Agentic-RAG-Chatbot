from langchain_community.vectorstores import Chroma

from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI

class VectorDB:
    """
    A class representing a vector database with a retriever.
    """

    def __init__(self, documents, collection_name="rag-chroma", model="mistral-embed"):
        """
        Initializes the VectorDB instance.

        Args:
        - documents (list): A list of documents to be indexed in the vector database.
        - collection_name (str, optional): The name of the collection in the vector database. Defaults to "rag-chroma".
        - model (str, optional): The model to use for embeddings. Defaults to "mistral-embed".
        """
        self.documents = documents
        self.collection_name = collection_name
        self.model = model
        self.embeddings = MistralAIEmbeddings(model=self.model)
        self.vectorstore = self._create_vectorstore()
        self.retriever = self.vectorstore.as_retriever()

    def _create_vectorstore(self):
        """
        Creates a Chroma vectorstore instance from the provided documents and embeddings.
        """
        return Chroma.from_documents(
            documents=self.documents,
            collection_name=self.collection_name,
            embedding=self.embeddings
        )
    
    def get_retriever(self):
        return self.retriever

# Example usage:
#documents = [...]  # Your list of documents
#vector_db = VectorDB(documents)
