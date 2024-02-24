from llama_cpp import Llama

def main():
    # Initialize and load the model
    llm = Llama(
        model_path="./llama-2-7b-chat.Q8_0.gguf",
        verbose=False
    )

    # Interactive prompt loop
    while True:
        prompt = input("Enter a prompt (or type 'exit' to quit): ")
        if prompt.lower() == "exit":
            break

        # Generate text based on the prompt
        output = llm(
            prompt,
            max_tokens=None,
            stop=["Q:", "\n"],
            echo=False
        )

        # Print the generated output
        print(output['choices'][0]['text'])

if __name__ == "__main__":
    main()

