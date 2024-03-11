from dataclasses import dataclass
from Classes.User import User
@dataclass(frozen=True)
class Profile:
    profile_id: int
    user_id: int
    bio: str
    recommendations: list['User']