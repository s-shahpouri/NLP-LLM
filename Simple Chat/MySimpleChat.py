from openai import OpenAI

class MySimpleChat:
    def __init__(self, chat_model):
        self.chat_model = chat_model
        self.embedding_model = "all-minilm"
        self.messages = [
            {"role": "assistant", "content": "You are a helpful personal assistant. Please respond concisely with complete sentences within the given token limit."},
            {"role": "user", "content": "Your prompt here"}
        ]

        if not self.chat_model:
            self.chat_model = "llama2"

        self.client = OpenAI(
            base_url = 'http://localhost:11434/v1',
            api_key='ollama', # required, but unused
        )

    def chat(self, message):
        user_msg = {
            "role": "user",
            "content": message
        }

        self.messages.append(user_msg)
        # print(self.messages)
        response = self.client.chat.completions.create(
            model=self.chat_model,
            messages=self.messages,
            stream=False,
            temperature=0.5,
            max_tokens=100,
        )

        system_response = {
            "role":"assistant",
            "content": response.choices[0].message.content
        }
        self.messages.append(system_response)
        return response.choices[0].message.content

