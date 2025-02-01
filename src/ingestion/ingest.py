import logging
from dotenv import load_dotenv

from src.config.config import conf

from loader import Loader
from preprocessor import Splitter

load_dotenv()

# create logger
logger = logging.getLogger("ingest")
logger.setLevel(conf.logging.level)

# define handler and formatter
handler = logging.StreamHandler()
formatter = logging.Formatter(
    conf.logging.format,
    datefmt=conf.logging.date_format
)

# add formatter to handler
handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(handler)


def ingest():
    logger.info("Started ingesting documents")

    path = conf.vector_store.ingestion.path_to_documents
    chunk_size = conf.vector_store.ingestion.chunk_size
    chunk_overlap = conf.vector_store.ingestion.chunk_overlap

    splitter = Splitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    logger.info("Splitting documents...")
    docs = splitter.split(path)

    for chunk in docs:
        source = chunk.metadata["source"]
        new_source = source.replace("langchain-docs", "https:/")
        chunk.metadata.update({"source": new_source})

    logger.info("Finished splitting documents")

    index_name = conf.vector_store.index_name
    embedding_model = conf.vector_store.embedding_model

    loader = Loader(index_name=index_name, embedding_model=embedding_model)

    logger.info("Loading documents...")
    loader.load(docs)
    logger.info("Finished loading documents")


if __name__ == "__main__":
    ingest()
