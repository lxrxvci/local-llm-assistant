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

## 📦 Getting Started & Installation

### 1. Prerequisites (The AI Engine)
Before running the Python code, you must install the Ollama engine and download the local models.
* Install Ollama from [ollama.com](https://ollama.com/) (or run `brew install ollama` on macOS).
* Start the Ollama server in your terminal:
  ```bash
  ollama serve
* Open a new terminal tab and download the required models:
	ollama pull llama3.2
	ollama pull nomic-embed-text

## 📦 Python Environment Setup
* Clone the repository (Replace YOUR-USERNAME with your actual GitHub username)
git clone [https://github.com/YOUR-USERNAME/local-llm-assistant.git](https://github.com/YOUR-USERNAME/local-llm-assistant.git)
cd local-llm-assistant

* Create and activate a virtual environment:
python3.11 -m venv venv
source venv/bin/activate

* Install Dependencies:
**INSIDE YOUR VIRTUAL ENVIRONMENT (VENV)**
pip install -r requirements.txt

## 🏃‍♂️ How to Run
Make sure your Ollama server is running in the background (ollama serve) and your virtual environment is active, then launch either script:

To run the Agent (Tool Calling & File Creation):
python agent.py

Ask the AI to write a poem, create a code snippet, or generate notes. It will automatically detect the request and write a .txt file to your local drive.

To run the RAG Pipeline (Secure Document Search):
python rag.py

The AI will read your local secret_memo.txt, store it in the Vector DB, and strictly answer questions based on the embedded knowledge.
