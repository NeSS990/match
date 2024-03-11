# chat_repository.py
class ChatRepository:
    def __init__(self):
        self.chats = []

    def save_chat(self, chat):
        self.chats.append(chat)

    def find_chat_by_id(self, chat_id):
        for chat in self.chats:
            if chat.chat_id == chat_id:
                return chat
        return None
