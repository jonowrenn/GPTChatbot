from openai import OpenAI
import gradio as gr
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

# ── Mode definitions ─────────────────────────────────────────────────────────

MODES = {
    "General": (
        "You are a friendly, concise, and helpful AI assistant. "
        "Prefer short paragraphs and bullet points when useful. Use concrete examples."
    ),
    "Explain a Concept": (
        "You are an expert CS and ML tutor. When asked to explain something, give a clear, "
        "structured explanation: start with an intuitive one-sentence summary, then explain "
        "the mechanics, then give a concrete example. Use analogies where helpful. "
        "Assume the student has introductory CS knowledge."
    ),
    "Code Review": (
        "You are a senior software engineer doing a thorough code review. "
        "Identify bugs, edge cases, performance issues, and style problems. "
        "Be specific — quote the relevant lines and explain why each issue matters. "
        "Also highlight what the code does well. End with a prioritized list of changes."
    ),
    "Debug Help": (
        "You are an expert debugger. Help the user find the root cause of their bug. "
        "Ask clarifying questions if needed. Walk through the logic step by step. "
        "Explain why the bug occurs, not just how to fix it."
    ),
    "ML Theory": (
        "You are a machine learning researcher and educator. Explain ML concepts rigorously "
        "but accessibly. Use math notation when it adds clarity (e.g. loss functions, "
        "gradient derivations). Connect theory to practical implications. "
        "Assume the student knows linear algebra and basic calculus."
    ),
    "Interview Prep": (
        "You are a technical interview coach. Help the user practice CS interview questions. "
        "For coding problems: clarify the problem, walk through examples, discuss "
        "time/space complexity, and suggest optimal approaches. "
        "For conceptual questions: give model answers and highlight what interviewers look for. "
        "Be encouraging but honest about gaps."
    ),
}

MODE_NAMES = list(MODES.keys())


def build_messages(history, user_msg, mode):
    system_prompt = MODES.get(mode, MODES["General"])
    messages = [{"role": "system", "content": system_prompt}]
    for turn in history[-10:]:
        if isinstance(turn, dict):
            messages.append({"role": turn["role"], "content": turn["content"]})
        else:
            u, a = turn
            if u: messages.append({"role": "user", "content": u})
            if a: messages.append({"role": "assistant", "content": a})
    messages.append({"role": "user", "content": user_msg})
    return messages


def respond(user_msg, history, mode):
    if not API_KEY:
        return "⚠️ **Error:** `OPENAI_API_KEY` is not set. Add it as a Space Secret or in a local `.env` file."
    try:
        messages = build_messages(history, user_msg, mode)
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ **Error:** {e}"


# ── UI ────────────────────────────────────────────────────────────────────────

with gr.Blocks(theme="soft", title="CS Study Assistant") as demo:
    gr.Markdown(
        "# 🎓 CS Study Assistant\n"
        "Ask about algorithms, data structures, ML concepts, or paste your code for review.\n\n"
        "Powered by **GPT-4o mini** · Switch modes to change how the assistant responds."
    )

    with gr.Row():
        mode = gr.Dropdown(
            label="Mode",
            choices=MODE_NAMES,
            value="General",
            scale=3,
        )
        clear_btn = gr.Button("🧹 New chat", variant="secondary", scale=1)

    mode_info = gr.Markdown(
        value=f"**General** — {MODES['General']}",
        elem_classes=["mode-info"],
    )

    chat = gr.ChatInterface(
        fn=respond,
        additional_inputs=[mode],
        title="",
        description="",
        textbox=gr.Textbox(
            placeholder="Ask a question or paste code...",
            lines=3,
            scale=1,
        ),
        retry_btn="↻ Regenerate",
        undo_btn="⟲ Undo",
        clear_btn=None,
    )

    # Update mode info blurb when mode changes
    def update_info(selected_mode):
        return f"**{selected_mode}** — {MODES.get(selected_mode, '')}"

    mode.change(fn=update_info, inputs=mode, outputs=mode_info)
    clear_btn.click(fn=lambda: [], inputs=None, outputs=chat.chatbot, queue=False)


if __name__ == "__main__":
    demo.launch()
