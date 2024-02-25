from Classes.Message import Message


class Chat:
    def __init__(self, chat_id, user_id):
        self.chat_id = chat_id
        self.user_id = user_id
        self._messages = []

    def send_message(self, message_id, content):
        self._messages.append(Message(message_id, self.chat_id, content))