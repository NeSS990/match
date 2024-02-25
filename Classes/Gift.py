from Classes.Message import Message
class Gift:
    def __init__(self, gift_id, name, price):
        self.gift_id = gift_id
        self.name = name
        self.price = price
        self._messages = []

    def add_message(self, message_id, content):
        self._messages.append(Message(message_id, None, content))