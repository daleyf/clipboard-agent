import time
import subprocess
import pyperclip
from rich.console import Console
from rich.panel import Panel

MODEL_NAME = "llama3.2:3b"
SYSTEM_PROMPT = "You are a personal PhD-level tutor who explains copied text clearly and concisely."
DELAY = 0.5


console = Console()


def run_llm(prompt: str) -> str:
    """Call the local LLM via Ollama with the given prompt."""
    result = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=f"{SYSTEM_PROMPT}\n\n{prompt}",
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def display_output(copied: str, explanation: str) -> None:
    """Render the copied text and explanation nicely."""
    console.clear()
    console.rule("[bold blue]ClipMind")
    console.print(Panel(copied, title="Copied Text", border_style="cyan"))
    console.print(Panel(explanation, title="Explanation", border_style="green"))


def main() -> None:
    """Continuously monitor the clipboard and explain new text."""
    last_text = ""
    console.print(
        "ClipMind running. Copy text to receive an explanation. Press Ctrl+C to exit."
    )

    try:
        while True:
            text = pyperclip.paste()
            if text and text != last_text:
                last_text = text
                with console.status("[bold green]Thinking..."):
                    response = run_llm(text)
                display_output(text, response)
            time.sleep(DELAY)
    except KeyboardInterrupt:
        console.print("\nExiting ClipMind.")


if __name__ == "__main__":
    main()
