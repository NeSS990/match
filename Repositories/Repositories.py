from abc import ABC, abstractmethod
import os
import json
from lxml import etree

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

class JSONRepository(BaseRepository):
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, data):
        with open(self.file_path, 'a') as f:  # Открытие файла в режиме добавления ('a')
            json.dump(data, f, ensure_ascii=False)
            f.write('\n')  # Добавление новой строки между записями

    def find(self, query):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        # Ваша логика поиска в JSON
        pass



class RelationalRepository(BaseRepository):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        # Ваша логика инициализации подключения к реляционной базе данных
        pass

    def save(self, data):
        # Ваша логика сохранения данных в реляционной базе данных
        pass

    def find(self, query):
        # Ваша логика поиска данных в реляционной базе данных
        pass

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

class RepositoryFactory(ABC):
    @abstractmethod
    def create_repository(self) -> BaseRepository:
        pass

class XMLRepositoryFactory(RepositoryFactory):
    def __init__(self, file_path):
        self.file_path = file_path

    def create_repository(self) -> BaseRepository:
        return XMLRepository(self.file_path)

class JSONRepositoryFactory(RepositoryFactory):
    def __init__(self, file_path):
        self.file_path = file_path

    def create_repository(self) -> BaseRepository:
        return JSONRepository(self.file_path)

class RelationalRepositoryFactory(RepositoryFactory):
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def create_repository(self) -> BaseRepository:
        return RelationalRepository(self.connection_string)
