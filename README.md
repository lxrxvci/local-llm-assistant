# 🧠 Local AI Assistant: RAG & Agentic Tool Calling

A 100% offline, privacy-first AI pipeline built for Apple Silicon (M4). This project demonstrates two advanced foundational AI architectures: **Retrieval-Augmented Generation (RAG)** and **Agentic Tool Calling**, all powered locally without any external cloud APIs.

## 🚀 Key Features

### 1. Agentic AI (Tool Calling)
* **Autonomous Execution:** The Llama 3 model is equipped with a custom system prompt and a tool registry, allowing it to decide when to take action.
* **Local File Operations:** Demonstrates the AI's ability to trigger local Python functions (like creating and writing to `.txt` files) based on conversational context.

### 2. Privacy-First RAG Pipeline
* **Total Privacy:** All inference and vector search happens strictly locally on-device.
* **Semantic Search:** Utilizes `nomic-embed-text` to convert private documents into math vectors for highly accurate context retrieval.
* **Vector Database:** Integrates `ChromaDB` for rapid, in-memory document querying.

## 🛠️ Technology Stack
* **Language:** Python 3.11
* **LLM Engine:** Ollama (Llama 3.2, Nomic-Embed-Text)
* **Database:** ChromaDB

## 📦 How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt