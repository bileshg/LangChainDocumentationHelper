import logging
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader, WikipediaLoader
from langchain_core.documents import Document

logger = logging.getLogger(__name__)


class Splitter:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, raw_documents: list[Document]) -> list[Document]:
        splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        return splitter.split_documents(raw_documents)


def read_the_docs(path: str | Path) -> list[Document]:
    loader = ReadTheDocsLoader(path=path, encoding="utf-8")
    return loader.load()

def read_wikipedia(query: str, max_docs: int = 25, content_max_chars: int = 4000) -> list[Document]:
    loader = WikipediaLoader(query=query, load_max_docs=max_docs, doc_content_chars_max=content_max_chars)
    return list(loader.lazy_load())
