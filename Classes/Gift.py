from dataclasses import dataclass

from Classes.Message import Message
@dataclass(frozen=True)
class Gift:
    gift_id: int
    name: str
    price: int
    messages: list['Message']