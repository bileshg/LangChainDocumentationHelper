import logging
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

logger = logging.getLogger(__name__)


class Loader:
    def __init__(self, index_name: str, embedding_model: str):
        self.index_name = index_name
        self.embeddings = OpenAIEmbeddings(model=embedding_model)

    def load(self, docs: list):
        PineconeVectorStore.from_documents(
            docs,
            index_name=self.index_name,
            embedding=self.embeddings
        )
