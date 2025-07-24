from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.1)
classifier_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an intelligent router. Classify the user's input into one of the following categories:

- 'codegen': For requests that involve writing, modifying, or generating code.
- 'error': For requests that involve explaining or fixing errors.
- 'rag': For general Appwrite documentation Q&A or how-to questions and tell about questions.
- 'planner': For requests that involve setup instructions, configuration, or step-by-step guides.

Respond with only one word: codegen, error, rag, or planner.
"""),

    # 🎯 Example 1
    ("user", "Can you write code to upload a file to Appwrite using Python?"),
    ("assistant", "codegen"),

    # 🎯 Example 2
    ("user", "I'm getting 'StoragePermissionDenied' when uploading a file. What does it mean?"),
    ("assistant", "error"),

    # 🎯 Example 3
    ("user", "How do I set up OAuth with GitHub in Appwrite?"),
    ("assistant", "planner"),

    # 🎯 Example 4
    ("user", "Tell me how Appwrite databases work."),
    ("assistant", "rag"),

    # 🎯 Example 5
    ("user", "Generate a Dart function to login using Appwrite"),
    ("assistant", "codegen"),

    # 🎯 Example 6
    ("user", "I get a 403 forbidden when calling the Appwrite API"),
    ("assistant", "error"),

    # ✅ Real user input goes here
    ("user", "{input}"),
])


classification_chain = (
    classifier_prompt
    | llm
    | RunnableLambda(lambda x: x.content.strip().lower())
)