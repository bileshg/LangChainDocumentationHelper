import logging

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_core.documents import Document

logger = logging.getLogger(__name__)


class Splitter:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, path: str) -> list[Document]:
        loader = ReadTheDocsLoader(path=path, encoding="utf-8")
        splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)

        raw_documents = loader.load()
        return splitter.split_documents(raw_documents)
