from src.config.config import conf
from src.rag.core import RagPipeline


QnA = RagPipeline(
    index_name=conf.vector_store.index_name,
    embedding_model=conf.vector_store.embedding_model,
    chat_model=conf.llm.chat_model_name,
    summarization_model=conf.llm.summarization_model_name
)


def main():
    print("AI: Hello! I am LangChain's AI assistant. Ask me anything about LangChain!")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            print("AI: Goodbye!")
            break

        response = QnA.run(user_input)

        print(f"AI: {response['answer']}")


if __name__ == "__main__":
    main()
