import logging
from pathlib import Path
from dotenv import load_dotenv
from src.config.config import conf
from vector_store import Loader
from preprocessor import Splitter, read_the_docs, read_wikipedia

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

    path = Path(conf.docs.local_directory).resolve()
    chunk_size = conf.vector_store.ingestion.chunk_size
    chunk_overlap = conf.vector_store.ingestion.chunk_overlap


    raw_docs = []

    logger.info("Reading Wikipedia...")
    raw_docs.extend(read_wikipedia("LangChain"))
    logger.info("Finished reading Wikipedia")

    logger.info("Reading documents...")
    raw_docs.extend(read_the_docs(path))
    logger.info("Finished reading documents")

    logger.info(f"Splitting {len(raw_docs)} raw documents...")
    splitter = Splitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = splitter.split(raw_docs)

    for chunk in docs:
        source = chunk.metadata["source"]
        new_source = source.replace(str(path), path.name).replace(conf.docs.local_directory, path.name)
        chunk.metadata.update({"source": new_source})

    logger.info("Finished splitting raw documents")

    index_name = conf.vector_store.index_name
    embedding_model = conf.vector_store.embedding_model

    vector_store = Loader(index_name=index_name, embedding_model=embedding_model)

    logger.info(f"Loading {len(docs)} document chunks to vector store...")
    vector_store.load(docs)
    logger.info("Finished loading documents")


if __name__ == "__main__":
    ingest()
