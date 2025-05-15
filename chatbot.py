from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Chatbot:
    def __init__(self, model_name="facebook/blenderbot-400M-distill", max_history_turns=3):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.conversation_history = []
        self.max_history_turns = max_history_turns

    def trim_history(self):
        max_len = self.max_history_turns * 2
        self.conversation_history = self.conversation_history[-max_len:]

    def build_history_string(self):
        lines = []
        for i, text in enumerate(self.conversation_history):
            speaker = "[User]" if i % 2 == 0 else "[Bot]"
            lines.append(f"{speaker}: {text}")
        return "\n".join(lines)

    def generate_response(self, input_text):
        if input_text.strip().lower() == "/reset":
            self.conversation_history = []
            return "Conversation history reset. How can I help you?"

        self.trim_history()
        history_string = self.build_history_string()
        inputs = self.tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
        self.conversation_history.append(input_text)
        self.conversation_history.append(response)

        return response

