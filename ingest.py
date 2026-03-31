"""
Knowledge ingestion pipeline.

Loads documents from data/ directory, splits into chunks,
generates embeddings, and saves the index to disk.

Usage: python ingest.py
"""

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, TextLoader
from langchain_core.documents import Document

from config import settings

directory = f"./{settings.data_dir}/"

loaders = {
    "PDF": DirectoryLoader(
        directory,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=not settings.skip_details,
        silent_errors=not settings.skip_details,
    ),
    "TXT": DirectoryLoader(
        directory,
        glob="**/*.txt",
        loader_cls=TextLoader,
        show_progress=not settings.skip_details,
        silent_errors=not settings.skip_details,
    ),
    "MD": DirectoryLoader(
        directory,
        glob="**/*.md",
        loader_cls=TextLoader,
        show_progress=not settings.skip_details,
        silent_errors=not settings.skip_details,
    ),
}


def ingest():
    # TODO:
    # 1. Load documents from config.data_dir (PDF, TXT, MD)
    # 2. Split into chunks using TextSplitter
    # 3. Generate embeddings
    # 4. Build vector store (FAISS, Qdrant, Chroma, etc.)
    # 5. Save index to config.index_dir
    # 6. Save chunks for BM25 retriever (pickle or JSON)

    documents = load_documents()

    pass


def load_documents() -> list[Document]:
    documents: list[Document] = []

    for file_type, loader in loaders.items():
        print(F"📂 Loading {file_type} documents from '{directory}' directory using {loader.loader_cls.__name__}")

        loaded_docs = loader.load()
        documents.extend(loaded_docs)

        print(f"📄 Loaded {len(loaded_docs)} pages from {file_type} files")
        print()
        print_loaded_docs_details(loaded_docs)

    return documents


def print_loaded_docs_details(langchain_docs: list[Document]):
    if settings.skip_details:
        return

    for doc in langchain_docs:
        print(f"  Page: {doc.metadata['page']} | Length: {len(doc.page_content)} chars")

    print()

if __name__ == "__main__":
    ingest()
