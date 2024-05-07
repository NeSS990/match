from datetime import datetime, timedelta
from Classes.Classes import Chat, Match, User
class BusinessRulesService:
    def __init__(self, chat_repository, match_repository, user_repository):
        self.chat_repository = chat_repository
        self.match_repository = match_repository
        self.user_repository = user_repository

    def apply_business_rules(self, user1_id, user2_id):
        self.remove_duplicate_recommendation(user1_id, user2_id)
        self.check_likes(user1_id, user2_id)

    def remove_duplicate_recommendation(self, user1_id, user2_id):
        user1_recommendations = self.user_repository.get_recommendations(user1_id)
        if user1_id in user1_recommendations:
            user1_recommendations.remove(user1_id)
        user2_recommendations = self.user_repository.get_recommendations(user2_id)
        if user2_id in user2_recommendations:
            user2_recommendations.remove(user2_id)
        self.user_repository.update_recommendations(user1_id, user1_recommendations)
        self.user_repository.update_recommendations(user2_id, user2_recommendations)

    def check_likes(self, user1_id, user2_id):
        if self.user_repository.check_like(user1_id, user2_id) and self.user_repository.check_like(user2_id, user1_id):
            match = Match(user1_id, user2_id)
            self.match_repository.save_match(match)
            chat = Chat(user1_id, user2_id)
            self.chat_repository.save_chat(chat)
        else:
            self.user_repository.remove_like(user1_id, user2_id)
            self.user_repository.remove_like(user2_id, user1_id)

    def remove_inactive_chats(self):
        now = datetime.now()
        for chat in self.chat_repository.chats:
            if (now - chat.last_activity_time) > timedelta(hours=24):
                self.chat_repository.chats.remove(chat)
    def like(self, user: User, liked_user_id: int):
        if user.user_id == liked_user_id:
            print("Error: You cannot like yourself.")
            return None
        else:
            user.likes.append(liked_user_id)
            return user
    