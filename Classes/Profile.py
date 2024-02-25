class Profile:
    def __init__(self, profile_id, user_id, bio):
        self.profile_id = profile_id
        self.user_id = user_id
        self.bio = bio
        self.recommendations = []