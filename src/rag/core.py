import logging
from typing import Any

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.memory import ConversationSummaryMemory

logger = logging.getLogger(__name__)

load_dotenv()


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


class RagPipeline:

    def __init__(self, index_name: str, embedding_model: str, chat_model: str, summarization_model: str):
        # Initialize embeddings for the document search.
        embeddings = OpenAIEmbeddings(model=embedding_model)

        # Initialize the vector store for document retrieval.
        vector_store = PineconeVectorStore(index_name=index_name, embedding=embeddings)

        # Configure the LLM chat model.
        chat_llm = ChatOpenAI(model=chat_model, verbose=True, temperature=0)

        # Configure the summarizer model.
        summarizer_llm = ChatOpenAI(model=summarization_model, verbose=True, temperature=0)

        # Use ConversationBufferMemory to maintain chat history
        memory = ConversationSummaryMemory(
            llm=summarizer_llm,
            memory_key="chat_history",
            output_key="answer",
            return_messages=True
        )

        self._qa = RetrievalQAWithSourcesChain.from_chain_type(
            llm=chat_llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(),
            memory=memory  # Add memory to track conversation history
        )

    def run(self, query: str) -> Any:
        # Invoke the pipeline with the query and chat history.
        return self._qa.invoke({"question": query})
