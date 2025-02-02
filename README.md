# LangChain Documentation Helper

This project is a LangChain Documentation Helper, designed to assist users in querying and retrieving information about LangChain documentation. It leverages Streamlit for the user interface and integrates with OpenAI large language models (LLMs) and Pinecone vector store to provide accurate and relevant answers.

## Features

- **Modern User Interface**: The application is built using Streamlit, providing a modern and interactive user interface.
- **Document Ingestion**: Documents can be ingested into the vector store to enable querying.
- **RAG-based Querying**: The application uses the RAG (Retrieval-Augmented Generation) model to provide accurate and relevant answers to user queries.
- **Conversation History**: The application maintains a history of user queries and responses for a more interactive experience.
- **Logging and Configuration**: The application supports logging and configuration through the `config.yaml` file.

## Requirements

- Python 3.7+
- OpenAI API key
- Pinecone API key

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/bileshg/LangChainDocumentationHelper.git
    cd LangChainDocumentationHelper
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    ```sh
   cp .env.example .env  # On Windows, use `copy .env.example .env`
    ```
   Provide your OpenAI and Pinecone API keys in the `.env` file.

## Configuration

Edit the `config.yaml` file to configure logging, document paths, vector store settings, and language models.

## Usage

### Downloading Documents

Download the LangChain documentation and save it in the `data` directory.
```sh
python src/download/download.py
```

### Ingesting Documents

To ingest documents into the vector store:
```sh
python src/ingestion/ingest.py
```

### Running the Application

To start the Streamlit application:
```sh
streamlit run src/app.py
```

## Project Structure

- `src/download/download.py`: Script for downloading documents.
- `src/ingestion/ingest.py`: Script for ingesting documents into the vector store.
- `src/app.py`: Main application file for the Streamlit interface.
- `src/config/config.py`: Configuration file loader.
- `config.yaml`: Configuration settings for the project.

## Acknowledgements

Thanks to [Eden Marco](https://www.linkedin.com/in/eden-marco/) for the inspiration and the tutorial on which this project is based.
