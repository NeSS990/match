# match_repository.py
class MatchRepository:
    def __init__(self):
        self.matches = []

    def save_match(self, match):
        self.matches.append(match)

    def find_match_by_users(self, user1_id, user2_id):
        for match in self.matches:
            if (match.user1_id == user1_id and match.user2_id == user2_id) or \
               (match.user1_id == user2_id and match.user2_id == user1_id):
                return match
        return None
