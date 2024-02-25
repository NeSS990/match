from Classes.Profile import Profile
class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self._profile = None
        self.likes = []

    def create_profile(self, profile_id, bio):
        self._profile = Profile(profile_id, self.user_id, bio)