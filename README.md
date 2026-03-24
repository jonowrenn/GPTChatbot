# 🎓 CS Study Assistant

A specialized AI study tool for computer science students, built with **Gradio** and **GPT-4o mini**.

**Live demo on Hugging Face Spaces:**
👉 [https://huggingface.co/spaces/jonowrenn/cs-study-assistant](https://huggingface.co/spaces/jonowrenn/cs-study-assistant)

> ⚠️ The live demo requires an OpenAI API key set as a Space Secret.
> To run locally, clone the repo and add your own key.

---

## Features

- **6 expert modes**, each with a tailored system prompt:
  - **General** — friendly, concise assistant for any question
  - **Explain a Concept** — structured explanations with intuition, mechanics, and examples
  - **Code Review** — senior-engineer-style review: bugs, edge cases, style, complexity
  - **Debug Help** — step-by-step root cause analysis
  - **ML Theory** — rigorous ML/math explanations for students who know linear algebra and calculus
  - **Interview Prep** — coding and conceptual interview coaching with complexity analysis
- Powered by **GPT-4o mini** for fast, high-quality responses
- Multi-turn conversation memory (last 10 turns)
- Compatible with Gradio 4.x and 5.x

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

1. Push the repo files to a Hugging Face Space (Gradio SDK)
2. Add your `OPENAI_API_KEY` under **Settings → Repository Secrets**
3. The app launches automatically

---

## Tech Stack

- Python
- [Gradio](https://gradio.app) — UI framework
- [OpenAI Python SDK](https://github.com/openai/openai-python) — GPT-4o mini
