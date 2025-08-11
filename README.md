# clipboard-agent

**Clipboard-Powered Personal AI Assistant for macOS**  
_On every copy, get a PhD-level explanation — instantly._

---

## Overview
ClipMind is a background process for macOS that listens to your clipboard and calls a **local LLM** whenever new text is copied.  
It’s tuned as a **personal, PhD-level intelligence** that explains things clearly and concisely.

If you’re reading Python docs (or anything else) and get stuck:
1. Copy the confusing text.
2. ClipMind detects it instantly.
3. The AI explains it to you in a clear, direct way — either in terminal or a UI pop-up.

No cloud calls. No data leaks. 100% local.

---

## Features
- **Instant AI Help** – Every copy triggers an AI response automatically.
- **Local-Only** – Works with Ollama, llama.cpp, or any other local LLM.
- **Clear Explanations** – System prompt tuned for precise, understandable answers.
- **Language-Agnostic** – Works on docs, research papers, emails, or any text.
- **Simple Setup** – No heavy dependencies or complex installs.

---

## Example Workflow
1. You’re reading the Python documentation for `asyncio`.
2. You copy the section about `asyncio.run()` and its event loop behavior.
3. ClipMind sees the change and calls your local LLM.
4. The AI responds:
    ```
    asyncio.run() sets up the event loop for you, runs the provided coroutine until complete,
    then closes the loop. This means you don’t need to manually manage the event loop unless
    you have multiple coroutines running in parallel.
    ```

---

## Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/clipmind.git
cd clipmind
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Requirements:

pyperclip (clipboard access)

A local LLM CLI tool (Ollama recommended)

Install Ollama:

bash
Copy
Edit
brew install ollama
ollama pull llama3  # or your preferred model
Usage
Run ClipMind:

bash
Copy
Edit
python clipmind.py
Copy any text — the AI will respond in your terminal.

Configuration
In clipmind.py, you can adjust:

MODEL_NAME → the model you want to use (llama3, mistral, etc.)

SYSTEM_PROMPT → sets AI personality (defaults to "You are a personal PhD-level tutor...")

DELAY → clipboard polling rate in seconds (default 0.5)

Privacy
Your clipboard is never sent to the cloud.
All AI calls are local, and no data leaves your machine.

Roadmap
 macOS menu bar UI

 Desktop notifications instead of terminal-only output

 Configurable trigger hotkey (manual mode)

 Support for Windows/Linux

License
MIT License © 2025 Your Name

pgsql
Copy
Edit

---

I kept it **developer-friendly but clear for non-tech users** so you could drop it into a public repo without extra editing.  

If you want, I can also add a **prompt-engineering section** in the README showing the exact *PhD-level explanation* system prompt so contributors can tweak it. That’d make the repo more self-documenting.  

Do you want me to add that section?
