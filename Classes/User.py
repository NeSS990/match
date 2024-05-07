
class User:
    def __init__(self, user_id, username, profile, likes=None):
        self.user_id = user_id
        self.username = username
        self.profile = profile
        self.likes = likes if likes is not None else []

    def serialize(self, serializer):
        serializer.start_object('user', self.user_id)
        serializer.add_property('username', self.username)
        serializer.add_property('profile', self.profile)
        serializer.add_property('likes', self.likes)

