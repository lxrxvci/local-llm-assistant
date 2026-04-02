import ollama
import os

# 1. Define the "Tool" (A standard Python function)
def create_text_file(filename: str, content: str) -> str:
    """
    Creates a new text file on the user's computer. 
    
    Args:
        filename (str): The exact name of the file, including the .txt extension (e.g., 'poem.txt').
        content (str): The actual generated text, poem, or code that will go inside the file. Do NOT output JSON schema here, only output the raw text.
    """
    try:
        # Create a folder to keep things organized
        os.makedirs("agent_outputs", exist_ok=True)
        filepath = os.path.join("agent_outputs", filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"SUCCESS: Wrote file to {filepath}"
    except Exception as e:
        return f"ERROR: Failed to write file. {str(e)}"

def main():
    print("🤖 Booting up Llama 3.2 Agent Mode...")
    print("Ask me to write a poem, create a code file, or take notes!")
    print("Type 'quit' to exit.\n")
    
    # --- THE FIX: We give the Agent strict instructions ---
    messages = [
        {
            "role": "system", 
            "content": """
            You are a helpful AI agent with access to tools. 
            When a user asks you to create or save a file:
            1. You MUST use the `create_text_file` tool.
            2. Do NOT output raw JSON in your chat response.
            3. The `content` parameter must contain the FULL, actual text (like the full poem or code), NOT a description of it.
            """
        }
    ]
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit']:
            break
            
        messages.append({"role": "user", "content": user_input})
        
        print("Llama is thinking... ", end="", flush=True)
        response = ollama.chat(
            model='llama3.2',
            messages=messages,
            tools=[create_text_file]
        )
        
        if response.get('message', {}).get('tool_calls'):
            print("\n[🛠️  AGENT DECIDED TO USE A TOOL!]")
            
            for tool in response['message']['tool_calls']:
                if tool['function']['name'] == 'create_text_file':
                    args = tool['function']['arguments']
                    filename = args.get('filename')
                    content = args.get('content')
                    
                    print(f"   -> Creating file: {filename}")
                    
                    result = create_text_file(filename, content)
                    print(f"   -> {result}")
                    
                    messages.append(response['message'])
                    messages.append({'role': 'tool', 'content': result, 'name': 'create_text_file'})
                    
                    final_response = ollama.chat(model='llama3.2', messages=messages)
                    print(f"\nLlama: {final_response['message']['content']}")
                    messages.append(final_response['message'])
                    
        else:
            reply = response['message']['content']
            print(f"\nLlama: {reply}")
            messages.append(response['message'])

if __name__ == "__main__":
    main()
