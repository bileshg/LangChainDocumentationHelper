import streamlit as st
import engine

def format_sources(sources):
    return "\n".join(f"- {source}" for source in sources.split(","))


def format_response(response):
    if response["sources"]:
        return f'{response["answer"]}\n\nSources:\n{format_sources(response["sources"])}'
    else:
        return response["answer"]


def main():
    with st.sidebar:
        st.title("🦜🔗 LangChain Bot")
        st.subheader("A Chatbot for LangChain Documentation")
        st.caption("This project is a LangChain Documentation Helper, designed to assist users in querying and retrieving information about LangChain documentation. It leverages Streamlit for the user interface and integrates with various language models and vector stores to provide accurate and relevant answers.")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Ask me anything about Langchain!"):
        _render_chats(prompt)


def _render_chats(prompt):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = engine.QnA.run(prompt)

    print(response)

    formatted_response = format_response(response)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # st.markdown(response["answer"])
        st.markdown(formatted_response)

    # Add assistant response to chat history
    st.session_state.messages.append({
        "role": "assistant",
        "content": formatted_response
    })


if __name__ == "__main__":
    main()
