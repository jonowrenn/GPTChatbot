---
title: GPT Chatbot
emoji: 💬
colorFrom: indigo
colorTo: blue
sdk: gradio
app_file: app.py
pinned: false
---

# GPT Chatbot

A conversational AI chatbot built with **Gradio** and the **OpenAI API**.

**Live demo on Hugging Face Spaces:**
👉 [https://huggingface.co/spaces/jonowrenn/gpt-chatbot](https://huggingface.co/spaces/jonowrenn/gpt-chatbot)

> ⚠️ Note: The live demo requires an OpenAI API key set as a Space Secret.
> To run without limits, clone the repo and use your own key.

---

## Features

- Chat with GPT-3.5-turbo in a clean Gradio interface
- Optional topic dropdown to guide the assistant (CS topics, general, etc.)
- Remembers the last 10 turns of conversation
- Regenerate / undo last message buttons
- Works on Hugging Face Spaces and locally

---

## Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/jonowrenn/GPTChatbot.git
cd GPTChatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

Get a key at [platform.openai.com/api-keys](https://platform.openai.com/api-keys).

### 4. Run

```bash
python app.py
```

Then open [http://localhost:7860](http://localhost:7860) in your browser.

---

## Deploy to Hugging Face Spaces

1. Push this repo to a Hugging Face Space (Gradio SDK)
2. Add your `OPENAI_API_KEY` under **Settings → Repository Secrets**
3. The app will launch automatically

---

## Tech Stack

- Python
- [Gradio](https://gradio.app) — UI framework
- [OpenAI Python SDK](https://github.com/openai/openai-python) — GPT-3.5-turbo
