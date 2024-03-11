from Classes.Message import Message
class Chat:
    def __init__(self, chat_id, user1_id, user2_id):
        self.chat_id = chat_id
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.messages = []

    def like_profile(self, profile_id):
        if profile_id != self.user_id:  # Проверка на попадание своей анкеты
            self.likes.append(profile_id)

    def add_match(self, match):
        self.matches.append(match)

    def initiate_chat(self, other_user):
        # Логика инициации чата после мэтча
        pass

    def check_inactive_chats(self):
        # Логика удаления чатов без активности
        pass
    def __eq__(self, other):
        if isinstance(other, Chat):
            return (
                self.chat_id == other.chat_id and
                self.user_id == other.user_id and
                self._messages == other._messages
            )
        return False
