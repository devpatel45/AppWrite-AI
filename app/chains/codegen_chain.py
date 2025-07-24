from app.chains.rag_retriever import retrieve_docs
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from app.prompts.codegen_prompt import codegen_prompt
from dotenv import load_dotenv
from app.utils.timing import timing
load_dotenv()

llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.3
)

parser = StrOutputParser()

@timing("code_gen_chain")
def generate_code_snippet(query: str) -> str:
    docs = retrieve_docs(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = codegen_prompt.format(query=query, context=context)
    response = llm.invoke(prompt)
    return parser.invoke(response)

if __name__ == "__main__":
    query = "How do I upload a file to Appwrite storage using Node.js?"
    print(generate_code_snippet(query))