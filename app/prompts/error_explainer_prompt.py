from langchain.prompts import PromptTemplate

error_explainer_prompt = PromptTemplate.from_template("""
You are an expert Appwrite assistant. A developer is facing the following error or stack trace:

Error Message:
--------------
{error}

Based on the following documentation context, explain the cause of the error and suggest a fix.

Relevant Documentation Context:
-------------------------------
{context}

Explanation and Suggested Fix:
-------------------------------
""")
