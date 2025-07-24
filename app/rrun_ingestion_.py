from ingestion.urls import urls
from ingestion.runner import run_ingestion

if __name__ == "__main__":
    run_ingestion(urls=urls, persist_dir="./data/chroma")

