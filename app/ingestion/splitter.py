from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(docs, chunk_size:int = 750, overlap: int = 100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_documents(docs)