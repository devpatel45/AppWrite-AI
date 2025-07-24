from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore', category=DeprecationWarning)

import tensorflow as tf
tf.get_logger().setLevel('ERROR')

def load_vector_db(persist_dir="./data/chroma"):
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vectordb = Chroma(persist_directory=persist_dir, embedding_function=embedding)
    return vectordb

def retrieve_docs(query, k=3):
    query = str(query)  
    vectordb = load_vector_db()
    return vectordb.similarity_search(query, k)