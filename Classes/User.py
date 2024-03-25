
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    user_id: int
    username: str
    profile: str
    likes: list[int] = None
