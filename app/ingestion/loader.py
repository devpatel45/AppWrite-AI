from langchain_community.document_loaders import UnstructuredURLLoader

def load_urls(urls: list[str]):
    loader = UnstructuredURLLoader(urls=urls)
    return loader.load()