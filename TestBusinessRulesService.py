import unittest
from Classes.Classes import Match
from Services.Services import BusinessRulesService

class MockUserRepository:
    def __init__(self):
        self.user_recommendations = {}
        self.user_likes = {}

    def get_recommendations(self, user_id):
        return self.user_recommendations.get(user_id, [])

    def update_recommendations(self, user_id, recommendations):
        self.user_recommendations[user_id] = recommendations

    def check_like(self, user_id, liked_user_id):
        return liked_user_id in self.user_likes.get(user_id, [])

    def remove_like(self, user_id, liked_user_id):
        if liked_user_id in self.user_likes.get(user_id, []):
            self.user_likes[user_id].remove(liked_user_id)


class TestBusinessRulesService(unittest.TestCase):
    def test_removeduplicaterecommendation(self):
        user1_id = 1
        user2_id = 2
        chat_repository = MockChatRepository()
        match_repository = MockMatchRepository()
        user_repository = MockUserRepository()
        business_service = BusinessRulesService(chat_repository, match_repository, user_repository)
        business_service.remove_duplicate_recommendation(user1_id, user2_id)
        self.assertNotIn(user1_id, user_repository.get_recommendations(user2_id))
        self.assertNotIn(user2_id, user_repository.get_recommendations(user1_id))

    def test_checklikescreatechat(self):
        user1_id = 1
        user2_id = 2
        chat_repository = MockChatRepository()
        match_repository = MockMatchRepository()
        user_repository = MockUserRepository()
        business_service = BusinessRulesService(chat_repository, match_repository, user_repository)
        match_repository.save_match(Match(user1_id, user2_id))
        business_service.check_likes(user1_id, user2_id)
        self.assertTrue(chat_repository.find_chat_by_users(user1_id, user2_id) is not None)

    def test_checklikesremoveprofiles(self):
        user1_id = 1
        user2_id = 2
        chat_repository = MockChatRepository()
        match_repository = MockMatchRepository()
        user_repository = MockUserRepository()
        business_service = BusinessRulesService(chat_repository, match_repository, user_repository)
        business_service.check_likes(user1_id, user2_id)
        self.assertNotIn(user2_id, user_repository.get_recommendations(user1_id))
        self.assertNotIn(user1_id, user_repository.get_recommendations(user2_id))

    def test_removeinactivechats(self):
        chat_repository = MockChatRepository()
        match_repository = MockMatchRepository()
        user_repository = MockUserRepository()
        business_service = BusinessRulesService(chat_repository, match_repository, user_repository)
        business_service.remove_inactive_chats()
        self.assertEqual(len(chat_repository.chats), 0)


class MockChatRepository:
    def __init__(self):
        self.chats = []

    def save_chat(self, chat):
        self.chats.append(chat)

    def find_chat_by_users(self, user1_id, user2_id):
        for chat in self.chats:
            if chat.user1_id == user1_id and chat.user2_id == user2_id:
                return chat
        return None

class MockMatchRepository:
    def __init__(self):
        self.matches = []
        self.user1_likes = []
        self.user2_likes = []

    def save_match(self, match):
        self.matches.append(match)

    def find_match_by_users(self, user1_id, user2_id):
        for match in self.matches:
            if (match.user1_id == user1_id and match.user2_id == user2_id) or \
               (match.user1_id == user2_id and match.user2_id == user1_id):
                return match
        return None
    
class MockUserRepository:
    def __init__(self):
        self.user_recommendations = {}
        self.user_likes = {}

    def get_recommendations(self, user_id):
        return self.user_recommendations.get(user_id, [])

    def update_recommendations(self, user_id, recommendations):
        self.user_recommendations[user_id] = recommendations

    def check_like(self, user_id, liked_user_id):
        return liked_user_id in self.user_likes.get(user_id, [])

    def remove_like(self, user_id, liked_user_id):
        if liked_user_id in self.user_likes.get(user_id, []):
            self.user_likes[user_id].remove(liked_user_id)

if __name__ == '__main__':
    unittest.main()
