import gradio as gr
from chatbot import Chatbot

bot = Chatbot()

def respond(user_input):
    return bot.generate_response(user_input)

# Build Gradio interface
iface = gr.Interface(
    fn=respond,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title="BlenderBot Chatbot",
    description="A simple chatbot powered by Hugging Face's BlenderBot model."
)

if __name__ == "__main__":
    iface.launch(share=True)
