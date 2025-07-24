from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
from typing import TypedDict
from app.semantic_classification import classification_chain

from app.chains.rag_chain import get_rag_response
from app.chains.codegen_chain import generate_code_snippet
from app.chains.error_explainer_chain import explain_error 
from app.chains.planner_chain import generate_plan

load_dotenv()

class GraphState(TypedDict):
    input: str
    category: str
    result: str


def classify_input(state: GraphState) -> GraphState:
    input_text = state["input"]
    raw = classification_chain.invoke({"input": input_text})
    category = raw.strip().lower()    # normalize case & strip whitespace
    print(f"🔍 Classifier returned: {category!r}")
    return {
        "input": input_text,
        "category": category,
        "result": ""
    }

def route_decision(state: GraphState) -> str:
    cat = state["category"]
    if cat in {"rag", "codegen", "error", "planner"}:
        return cat
    # fallback to a safe default (e.g. RAG Q&A)
    return "rag"


def run_rag(state: GraphState) -> GraphState:
    return {
        "input": state["input"],
        "category": state["category"],
        "result": get_rag_response(state["input"])
    }

def run_codegen(state: GraphState) -> GraphState:
    return {
        "input": state["input"],
        "category": state["category"],
        "result": generate_code_snippet(state["input"])
    }

def run_error(state: GraphState) -> GraphState:
    return {
        "input": state["input"],
        "category": state["category"],
        "result": explain_error(state["input"])
    }

def run_planner(state: GraphState) -> GraphState:
    return {
        "input": state["input"],
        "category": state["category"],
        "result": generate_plan(state["input"])
    }


builder = StateGraph(GraphState)


builder.add_node("classify", RunnableLambda(classify_input))
builder.add_node("rag", RunnableLambda(run_rag))
builder.add_node("codegen", RunnableLambda(run_codegen))
builder.add_node("error", RunnableLambda(run_error))
builder.add_node("planner", RunnableLambda(run_planner))

builder.set_entry_point("classify")
builder.add_conditional_edges("classify", route_decision, {
    "rag": "rag",
    "codegen": "codegen",
    "error": "error",
    "planner": "planner"
})
builder.add_edge("rag", END)
builder.add_edge("codegen", END)
builder.add_edge("error", END)
builder.add_edge("planner", END)


graph = builder.compile()

if __name__ == "__main__":
    while True:
        query = input("Ask: ")
        if query.lower() in ["exist", "quit"]:
            break
        result = graph.invoke({"input": query})
        print(result.get("result"))