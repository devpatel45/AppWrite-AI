from langchain_core.prompts import PromptTemplate

qa_prompt = PromptTemplate.from_template("""
You are an expert Appwrite assistant.

Use the context below to answer the developer's question. Be concise and developer-friendly.

Context:
---------
{context}

Question:
---------
{question}
""")
