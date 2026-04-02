import ollama
import chromadb

def main():
    print("1. 🧠 Initializing local Vector Database...")
    # This creates a temporary database in your Mac's memory
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="confidential_docs")

    print("2. 📄 Reading the top-secret memo...")
    with open("secret_memo.txt", "r") as file:
        document_text = file.read()

    print("3. 🔢 Converting text to math (Embedding)...")
    # We use the Nomic model to turn the text into an array of numbers
    embedding_response = ollama.embeddings(
        model="nomic-embed-text", 
        prompt=document_text
    )
    
    # Save it to our database
    collection.add(
        ids=["memo_1"],
        embeddings=[embedding_response["embedding"]],
        documents=[document_text]
    )
    print("   ✅ Memo securely stored in the Vector Database!\n")

    # --- THE MAGIC TRICK ---
    
    question = "What is the new office WiFi password?"
    print(f"You: {question}")
    
    # 1. Convert the user's question into math (vectors)
    question_embedding = ollama.embeddings(
        model="nomic-embed-text", 
        prompt=question
    )["embedding"]

    # 2. Search the database for the most mathematically similar text!
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=1
    )
    
    # We grab the matching text from our secret memo
    secret_context = results["documents"][0][0]
    
    # 3. Create a strict prompt for Llama 3
    system_prompt = f"""
    You are a highly secure AI assistant. You must ONLY use the provided context to answer the question. 
    If the answer is not in the context, say "I don't have clearance for that."
    
    CONTEXT: {secret_context}
    """

    print("Llama 3.2: ", end="", flush=True)
    
    # 4. Ask the model!
    stream = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        stream=True
    )
    
    for chunk in stream:
        print(chunk['message']['content'], end="", flush=True)
        
    print("\n" + "-"*50)

if __name__ == "__main__":
    main()
