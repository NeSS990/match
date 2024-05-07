from dataclasses import dataclass

@dataclass(frozen=True)
class Message:
    message_id: int
    chat_id: int
    sender_id: int
    content: str
    timestamp: str

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


@dataclass(frozen=True)
class Gift:
    gift_id: int
    name: str
    price: int
    messages: list[Message]

@dataclass(frozen=True)
class Profile:
    profile_id: int
    user_id: int
    bio: str
    recommendations: list[int]

class Chat:
    def __init__(self, chat_id, user1_id, user2_id):
        self.chat_id = chat_id
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.messages = []
    
    def __eq__(self, other):
        if isinstance(other, Chat):
            return (
                self.chat_id == other.chat_id and
                self.user1_id == other.user1_id and
                self.user2_id == other.user2_id
            )
        return False

class Match:
    def __init__(self, user1_id, user2_id):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.chat = None