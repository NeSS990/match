class Message:
    def __init__(self, message_id, chat_id, sender_id, content, timestamp):
        self.message_id = message_id
        self.chat_id = chat_id
        self.sender_id = sender_id
        self.content = content
        self.timestamp = timestamp
    def __eq__(self, other):
        if isinstance(other, Message):
            return (
                self.message_id == other.message_id and
                self.chat_id == other.chat_id and
                self.content == other.content
            )
        return False