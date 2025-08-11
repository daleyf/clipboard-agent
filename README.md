# ClipMind

Simple clipboard watcher that queries a local `llama3.2:3b` model through [Ollama](https://ollama.ai) and prints a short explanation for whatever you copy.

## Requirements

- Python 3.8+
- [Ollama](https://ollama.ai) with the `llama3.2:3b` model
- `pyperclip` (installed from `requirements.txt`)

## Installation

```bash
git clone https://github.com/yourusername/clipboard-agent.git
cd clipboard-agent
pip install -r requirements.txt
ollama pull llama3.2:3b
```

## Usage

Start the assistant:

```bash
python clipmind.py
```

Leave the terminal running. Whenever you copy text, the script sends it to `llama3.2:3b` and prints the model's explanation to the console.

## Configuration

You can edit `MODEL_NAME`, `SYSTEM_PROMPT`, or `DELAY` at the top of `clipmind.py` to change the model, adjust the tone, or tweak the polling interval.

## License

MIT
