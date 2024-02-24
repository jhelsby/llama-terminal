## LLaMa in Terminal

Simple utility to run LLaMA models in terminal.

1. Download a model. I used this [llama-2-7b-chat.Q8_0.gguf](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/) model.
2. Change the `model_path` parameters in [infer.py](/infer.py) and [assist.py](/assist.py) to point to your downloaded model.
3. With the latest version of Python installed, create and activate a virtual environment, then install `llama-cpp-python` using pip:
    ```bash
    python -m venv .venv
    source .venv/bin/activate # Use .venv\Scripts\activate for Windows
    pip install llama-cpp-python
    ```

4. Run `python assist.py` to use a chatbot interface, or `python infer.py` for sentence completion.