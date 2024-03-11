from datetime import datetime, timedelta
from Classes.Match import Match
from Classes.Chat import Chat
from Repositories.ChatRepository import ChatRepository
from Repositories.MatchRepository import MatchRepository
class ChatService:
    @staticmethod
    def initiate_chat(user1, user2):
        if user1.user_id != user2.user_id:
            match = Match(user1_id=user1.user_id, user2_id=user2.user_id)
            user1.add_match(match)
            user2.add_match(match)
            chat = Chat(chat_id=match.user1_id + match.user2_id, user1_id=match.user1_id, user2_id=match.user2_id)
            match.chat = chat
            ChatRepository.save_chat(chat)
            MatchRepository.save_match(match)
            return chat
        else:
            return None

    @staticmethod
    def check_inactive_chats():
        current_time = datetime.now()
        inactive_chats = []

        for chat in ChatRepository.chats:
            last_activity_time = max([message.timestamp for message in chat.messages] + [chat.created_at])
            if current_time - last_activity_time > timedelta(hours=24):
                inactive_chats.append(chat)

        for chat in inactive_chats:
            ChatRepository.chats.remove(chat)

