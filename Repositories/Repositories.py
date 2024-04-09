from abc import ABC, abstractmethod
from lxml import etree
import os

class BaseRepository(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def find(self, query):
        pass


class XMLRepository(BaseRepository):
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, data):
        # Создаем корневой элемент XML, если файл не существует
        if not os.path.exists(self.file_path):
            root = etree.Element("data")
            tree = etree.ElementTree(root)
            tree.write(self.file_path, xml_declaration=True, encoding='utf-8', pretty_print=True)
        
        # Добавляем новые данные в XML файл
        tree = etree.parse(self.file_path)
        root = tree.getroot()
        new_data_element = etree.Element("item")
        for key, value in data.items():
            child = etree.Element(key)
            child.text = str(value)
            new_data_element.append(child)
        root.append(new_data_element)
        tree.write(self.file_path, xml_declaration=True, encoding='utf-8', pretty_print=True)

    def find(self, query):
        tree = etree.parse(self.file_path)
        return tree.xpath(query)
    
class ChatRepository:
    def __init__(self):
        self.chats = []

    def save_chat(self, chat):
        self.chats.append(chat)

    def find_chat_by_id(self, chat_id):
        for chat in self.chats:
            if chat.chat_id == chat_id:
                return chat
        return None

class GiftRepository:
    def __init__(self):
        self.gifts = []

    def save_gift(self, gift):
        self.gifts.append(gift)

    def find_gift_by_id(self, gift_id):
        for gift in self.gifts:
            if gift.gift_id == gift_id:
                return gift
        return None

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
    

class UserRepository:
    def __init__(self):
        self.user_recommendations = {}
        self.user_likes = {}  # Словарь для хранения лайков

    def get_recommendations(self, user_id):
        return self.user_recommendations.get(user_id, [])

    def update_recommendations(self, user_id, recommendations):
        self.user_recommendations[user_id] = recommendations

    def check_like(self, user_id, liked_user_id):
        return liked_user_id in self.user_likes.get(user_id, [])

    def remove_like(self, user_id, liked_user_id):
        if liked_user_id in self.user_likes.get(user_id, []):
            self.user_likes[user_id].remove(liked_user_id)
