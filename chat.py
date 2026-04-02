import ollama

def main():
    print("🤖 Booting up Local Llama 3.2...")
    print("Type 'quit' to exit.\n")
    
    # We will keep a "memory" of the conversation
    messages = []
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
            
        # Add the user's message to the memory
        messages.append({"role": "user", "content": user_input})
        
        print("Llama: ", end="", flush=True)
        
        # Talk to the local model and stream the response word-by-word!
        response = ollama.chat(
            model='llama3.2',
            messages=messages,
            stream=True
        )
        
        # This loop prints the words as fast as the M4 chip generates them
        assistant_reply = ""
        for chunk in response:
            word = chunk['message']['content']
            print(word, end="", flush=True)
            assistant_reply += word
            
        print("\n" + "-"*50)
        
        # Save the AI's reply to the memory so it remembers the context
        messages.append({"role": "assistant", "content": assistant_reply})

if __name__ == "__main__":
    main()
