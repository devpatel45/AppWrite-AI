# ui/streamlit_app.py
import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from app.utils.metrics import get_metrics
from app.langgraph_router import graph

st.set_page_config(page_title="Appwrite AI Dev Assistant", page_icon="🧠")

st.title("🧠 Appwrite AI Dev Assistant")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask something about Appwrite...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    # Run through LangGraph
    with st.spinner("Thinking..."):
        result = graph.invoke({"input": user_input})
        output = result.get("result", "⚠️ No response generated.")

    # Display AI response
    with st.chat_message("ai"):
        st.markdown(output)

    st.session_state.messages.append({"role": "ai", "content": output})

with st.sidebar.expander("📊 Metrics"):
    st.json(get_metrics())
