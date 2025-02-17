from langchain_together import ChatTogether
from config import *
from db import *


messages: dict[int, list] = load_json("bot_memory.json")


class Ai:
    def __init__(self) -> None:
        self.ai = ChatTogether(
            name=AI_NAME,
            model=AI_MODEL,
            temperature=AI_TEMPERATURE,
            max_tokens=AI_MAX_TOKENS,
            api_key=TOGETHER_API_KEY,
        )
        
    def add_msg(self, id, role, msg):
        if messages.get(id) is None:
            messages[id] = []
        messages[id].append({"role": role, "content": msg})
        save_json(messages, "bot_memory.json")

    def ask(self, id: int, question: str) -> str:
        self.add_msg(id, USER_ROLE, question)

        fmt_messages= "\n".join([f"{msg["role"]}: {msg["content"]}" for msg in messages[id]])
        response = self.ai.invoke(fmt_messages)

        self.add_msg(id, AI_ROLE, response.content)

        return response.content
