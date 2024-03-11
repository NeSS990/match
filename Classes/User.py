from Classes.Profile import Profile
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    user_id: int
    username: str
    profile: 'Profile'
    likes: list[int] = None
