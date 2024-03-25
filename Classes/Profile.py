from dataclasses import dataclass



@dataclass(frozen=True)
class Profile:
    profile_id: int
    user_id: int
    bio: str
    recommendations: list
