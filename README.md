# 🧠 Local RAG Pipeline (Llama 3 + ChromaDB)

A 100% offline, privacy-first Retrieval-Augmented Generation (RAG) pipeline built for Apple Silicon (M4). This project demonstrates how to securely ground Large Language Models in private data without relying on external cloud APIs.

## 🚀 Features
* **Total Privacy:** All inference and vector search happens locally on-device.
* **Semantic Search:** Utilizes `nomic-embed-text` to convert documents into math vectors for highly accurate context retrieval.
* **Vector Database:** Integrates `ChromaDB` for rapid, in-memory document querying.
* **Local Inference:** Powered by Meta's `Llama 3.2` running seamlessly via the Ollama engine.

## 🛠️ Technology Stack
* **Language:** Python 3.11
* **LLM Engine:** Ollama (Llama 3.2, Nomic-Embed-Text)
* **Database:** ChromaDB

## 📦 How It Works
1. **Ingestion:** Private text documents are parsed and converted into embeddings.
2. **Storage:** Embeddings are stored in a local ChromaDB collection.
3. **Retrieval:** User queries are embedded and matched against the database using cosine similarity.
4. **Generation:** The exact matched context is injected into Llama 3's system prompt, restricting the model to answer *only* based on the provided secure data.