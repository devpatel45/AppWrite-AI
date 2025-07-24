
# 🧠 Appwrite AI Dev Assistant

A powerful AI assistant built to help developers understand and use the [Appwrite](https://appwrite.io/docs) backend platform. It uses RAG (Retrieval-Augmented Generation), code generation, error explanation, and intelligent task planning to answer questions about Appwrite’s APIs, SDKs, and setup.

> 💡 Designed to accelerate developer onboarding and debugging using LLMs like Mixtral via Groq.

---

## 🚀 Features

- 🔍 **RAG-based answering** from Appwrite docs using ChromaDB
- 🤖 **Code generation** based on user goals (e.g., "generate Appwrite auth code in Node.js")
- 🛠️ **Error explanation** using intelligent prompt analysis
- 🧭 **Setup planning** (e.g., “How do I integrate Appwrite with Flutter?”)
- 📊 **Usage & latency metrics** for observability
- ⚙️ Modular, testable LangChain + LangGraph pipeline

---

## 🧱 Architecture

```
                    ┌──────────────────────┐
                    │ Streamlit Frontend   │
                    └────────┬─────────────┘
                             ↓
                  ┌────────────────────┐
        ┌────────▶│ LangGraph Router    │◀────────┐
        │         └─────┬─────┬─────────┘         │
        │               │     │                   │
        │               ↓     ↓                   ↓
        │        ┌────────┐ ┌─────────────┐ ┌────────────┐
        │        │  RAG   │ │ Codegen     │ │ Error Expl.│
        │        └────────┘ └─────────────┘ └────────────┘
        │
        └─────> ChromaDB ←─ Markdown Ingestor (docs)
```

---

## 🧰 Tech Stack

| Layer         | Tech/Tools |
|---------------|------------|
| LLM Backend   | Groq + Llama |
| RAG & Chains  | LangChain, LangGraph |
| Embeddings    | HuggingFace  |
| Vector Store  | ChromaDB |
| Frontend      | Streamlit |
| Containerization | Docker |
| Testing       | `pytest` |
| Monitoring    | Custom JSON metrics |

---

## ⚙️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/devpatel/appwrite-ai-dev-assistant.git
cd appwrite-ai-dev-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup environment

make an `.env` file

```
.env     # contains the GROQ API key
```

### 4. Run the Streamlit app

```bash
streamlit run UI/Interface.py
```

### 5. Run ingestion (optional)

```bash
python app/ingestion/ingest_docs.py
```

---

## 🧪 Running Tests

```bash
pytest tests/
```

✅ Tests cover:
- Metric logging
- Chain output validation
- Semantic classification

---

## 📁 Folder Structure

```
appwrite-ai-dev-assistant/
├── app/
│   ├── ingestion/           # Ingests Appwrite docs
│   ├── chains/              # RAG, codegen, error explainer, planner
│   ├── api/                 # (Optional) Appwrite wrapper
│   └── prompts/             # System prompts
├── UI/                      # Streamlit UI
├── data/                    # Vector DB (Chroma) and cache
├── tests/                   # Unit tests
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---
