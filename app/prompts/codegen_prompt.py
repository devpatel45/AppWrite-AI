from langchain_core.prompts import PromptTemplate

codegen_prompt = PromptTemplate.from_template("""
You are an AI coding assistant specialized in Appwrite.

Based on the following context, generate a clear and complete code snippet that addresses the developer's query. 
Use the correct Appwrite SDK and relevant API calls.

Context:
---------
{context}

Query:
-------
{query}

Code:
------
""")
