from llama_cpp import Llama

def main():
    # Initialize and load the GGUF model
    llm = Llama(
        model_path="./llama-2-7b-chat.Q8_0.gguf",
        verbose=False
    )

    print("Welcome! I'm your AI assistant. You can start interacting with me by typing your questions or prompts.")

    # Interactive prompt loop
    while True:
        # Prompt user for input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Define a list of messages for the chat
        messages = [
            {"role": "system", "content": "You are an AI assistant who can answer a variety of questions."},
            {"role": "user", "content": user_input}
        ]

        # Generate chat completion based on the defined messages
        completion = llm.create_chat_completion(messages=messages)

        print(completion)

        # Extract the response from the completion and print it
        response_content = completion['choices'][0]['message']['content']
        print("AI:", response_content)

if __name__ == "__main__":
    main()
