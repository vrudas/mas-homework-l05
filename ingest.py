"""
Knowledge ingestion pipeline.

Loads documents from data/ directory, splits into chunks,
generates embeddings, and saves the index to disk.

Usage: python ingest.py
"""

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_core.documents import Document

from config import settings


def ingest():
    # TODO:
    # 1. Load documents from config.data_dir (PDF, TXT, MD)
    # 2. Split into chunks using TextSplitter
    # 3. Generate embeddings
    # 4. Build vector store (FAISS, Qdrant, Chroma, etc.)
    # 5. Save index to config.index_dir
    # 6. Save chunks for BM25 retriever (pickle or JSON)

    path_to_data = f"./{settings.data_dir}/"
    loader = DirectoryLoader(
        path=path_to_data,
        glob="**/*.pdf",
        show_progress=True,
        silent_errors=True,
        loader_cls=PyPDFLoader
    )

    print(F"📂 Loading documents from '{path_to_data}' directory using LangChain DirectoryLoader...")
    langchain_docs = loader.load()

    print(f"📄 Loaded {len(langchain_docs)} pages via LangChain PyPDFLoader")
    print_loaded_docs_details(langchain_docs)

    pass


def print_loaded_docs_details(langchain_docs: list[Document]):
    if settings.skip_details:
        return

    for doc in langchain_docs:
        print(f"  Page: {doc.metadata['page']} | Length: {len(doc.page_content)} chars")


if __name__ == "__main__":
    ingest()
