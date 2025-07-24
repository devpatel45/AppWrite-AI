from ingestion.loader import load_urls
from ingestion.splitter import split_documents
from ingestion.embedder import get_embedddings
from langchain_community.vectorstores import Chroma


def run_ingestion(urls: list[str], persist_dir: str):
    docs = load_urls(urls=urls)
    chunks = split_documents(docs=docs)
    emb = get_embedddings()
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=emb,
        persist_directory=persist_dir
    )
    vectordb.persist()
    print(f"Ingested {vectordb._collection.count()} chuncks")
    