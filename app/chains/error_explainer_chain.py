from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from app.chains.rag_retriever import retrieve_docs
from app.prompts.error_explainer_prompt import error_explainer_prompt
from dotenv import load_dotenv
from app.utils.timing import timing
load_dotenv()

llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.1)
parser = StrOutputParser()

@timing("error_explainer_chian")
def explain_error(error: str) -> str:
    docs = retrieve_docs(error)
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = error_explainer_prompt.format(error=error, context=context)
    response = llm.invoke(prompt)
    return parser.invoke(response)

if __name__ == "__main__":
    sample_error = "StoragePermissionDenied: You do not have permission to access this bucket."
    print(explain_error(sample_error))