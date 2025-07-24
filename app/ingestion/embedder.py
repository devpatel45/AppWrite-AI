from langchain_huggingface import HuggingFaceEmbeddings


def get_embedddings(model_name: str = "sentence-transformers/all-mpnet-base-v2"):
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )