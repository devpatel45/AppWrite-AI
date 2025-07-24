from app.chains.rag_retriever import retrieve_docs
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from app.prompts.planner_prompt import planner_prompt
from dotenv import load_dotenv
from app.utils.timing import timing
load_dotenv()

llm = ChatGroq(
    model_name="llama3-70b-8192",
    temperature=0
)

parser = StrOutputParser()

@timing("planner_chain")
def generate_plan(goal: str) -> str:
    docs = retrieve_docs(goal)
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = planner_prompt.format(goal=goal, context=context)
    response = llm.invoke(prompt)
    return parser.invoke(response)

if __name__ == "__main__":
    goal = "Build a GitHub OAuth login flow with Appwrite and Next.js"
    print(generate_plan(goal))