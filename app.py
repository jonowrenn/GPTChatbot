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

SYSTEM_PROMPT = (
    "You are a friendly, concise, and helpful AI assistant. "
    "Prefer short paragraphs, bullet points when useful, and concrete examples."
)

def build_messages(history, user_msg, topic):
    messages = [{"role": "system", "content": SYSTEM_PROMPT + (f" The current topic is: {topic}." if topic else "")}]
    for turn in history[-10:]:
        if isinstance(turn, dict):
            messages.append({"role": turn["role"], "content": turn["content"]})
        else:
            u, a = turn
            if u: messages.append({"role": "user", "content": u})
            if a: messages.append({"role": "assistant", "content": a})
    messages.append({"role": "user", "content": user_msg})
    return messages

def respond(user_msg, history, topic):
    if not API_KEY:
        return "⚠️ Error: OPENAI_API_KEY is not set. Add it as a Space Secret or in a local .env file."
    try:
        messages = build_messages(history, user_msg, topic)
        resp = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=0.7)
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

with gr.Blocks(theme="soft") as demo:
    gr.Markdown("# 💬 GPT Chatbot\nA simple, clean chatbot powered by OpenAI + Gradio.")
    with gr.Row():
        topic = gr.Dropdown(label="Optional topic context", choices=["", "General", "Data Structures", "Algorithms", "Linear Algebra", "Probability"], value="")
        clear_btn = gr.Button("🧹 New chat", variant="secondary")
    chat = gr.ChatInterface(fn=respond, additional_inputs=[topic], title="", description="Type a message below. Use the topic dropdown (optional) to guide the assistant.", textbox=gr.Textbox(placeholder="Ask me anything...", lines=2, scale=1), retry_btn="↻ Regenerate", undo_btn="⟲ Undo last", clear_btn=None)
    clear_btn.click(fn=lambda: [], inputs=None, outputs=chat.chatbot, queue=False)

if __name__ == "__main__":
    demo.launch()
