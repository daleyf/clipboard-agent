import time
import subprocess
import pyperclip

MODEL_NAME = "llama3.2:3b"
SYSTEM_PROMPT = "You are a personal PhD-level tutor who explains copied text clearly and concisely."
DELAY = 0.5


def run_llm(prompt: str) -> str:
    """Call the local LLM via Ollama with the given prompt."""
    result = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=f"{SYSTEM_PROMPT}\n\n{prompt}",
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def main() -> None:
    """Continuously monitor the clipboard and explain new text."""
    last_text = ""
    print("ClipMind running. Copy text to receive an explanation. Press Ctrl+C to exit.")

    try:
        while True:
            text = pyperclip.paste()
            if text and text != last_text:
                last_text = text
                response = run_llm(text)
                print("\nCopied text:\n" + text)
                print("\nExplanation:\n" + response + "\n")
            time.sleep(DELAY)
    except KeyboardInterrupt:
        print("\nExiting ClipMind.")


if __name__ == "__main__":
    main()
