import unittest
from datetime import datetime, timedelta
from Classes.User import User
from Classes.Message import Message
from Repositories.MatchRepository import MatchRepository
from Repositories.ChatRepository import ChatRepository
from Services.ChatService import ChatService


class TestChatService(unittest.TestCase):
    def setUp(self):
        self.user1 = User(user_id=1, username="user1")
        self.user2 = User(user_id=2, username="user2")

    def test_initiate_chat_successful(self):
        chat = ChatService.initiate_chat(self.user1, self.user2)
        self.assertIsNotNone(chat)
        self.assertEqual(len(self.user1.matches), 1)
        self.assertEqual(len(self.user2.matches), 1)

    def test_initiate_chat_same_user(self):
        chat = ChatService.initiate_chat(self.user1, self.user1)
        self.assertIsNone(chat)
        self.assertEqual(len(self.user1.matches), 0)

    def test_check_inactive_chats(self):
        # Создаем чат и отправляем сообщение
        chat = ChatService.initiate_chat(self.user1, self.user2)
        chat.messages.append(Message(message_id=1, chat_id=chat.chat_id, sender_id=self.user1.user_id, content="Hello"))

        # Перемещаем время вперед на 48 часов
        current_time = datetime.now() + timedelta(hours=48)
        ChatService.check_inactive_chats(current_time)

        # Проверяем, что чат удален из репозитория
        self.assertEqual(len(ChatRepository.chats), 0)


if __name__ == '__main__':
    unittest.main()
