from app.chains.rag_retriever import retrieve_docs
from app.prompts.rag_prompt import qa_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap, RunnablePassthrough
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from app.utils.timing import timing



load_dotenv()


llm = ChatGroq(
    model_name="llama3-70b-8192",
    temperature=0
)

def get_rag_chain():
    return (
        RunnableMap({
            "context": lambda x: "\n\n".join([doc.page_content for doc in retrieve_docs(x["question"])]),
            "question": RunnablePassthrough()
        })
        | qa_prompt
        | llm
        | StrOutputParser()
    )

@timing("rag_chain")
def get_rag_response(query: str) -> str:
    chain = get_rag_chain()
    return chain.invoke({"question": query})


if __name__ == "__main__":
    response = get_rag_response("What functionalities do appwrite provide?")
    print(response)