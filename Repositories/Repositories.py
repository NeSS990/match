from abc import ABC, abstractmethod
import os
import json
from lxml import etree
import mysql.connector
import xml.etree.ElementTree as et


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
class RelationalRepository:
    """Репозиторий для работы с реляционной базой данных."""

    def __init__(self, connection_string):
        self.connection_string = connection_string

    def save(self, user):
        # Подключаемся к базе данных
        connection = mysql.connector.connect(**self.connection_string)
        cursor = connection.cursor()

        # Выполняем SQL-запрос для сохранения пользователя
        cursor.execute("INSERT INTO users (user_id, username, profile, likes) VALUES (%s, %s, %s, %s)",
                       (user.user_id, user.username, user.profile, ','.join(map(str, user.likes))))

        # Фиксируем изменения и закрываем соединение
        connection.commit()
        connection.close()
class JSONRepository:
    """Репозиторий для сериализации в формат JSON."""

    def __init__(self, file_path):
        self.file_path = file_path

    def start_object(self, object_name, object_id):
        self._current_object = {'id': object_id}

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)

    def save(self, user):
        self.start_object('user', user.user_id)
        self.add_property('username', user.username)
        self.add_property('profile', user.profile)
        self.add_property('likes', user.likes)
        with open(self.file_path, 'w') as file:
            file.write(self.to_str())

class XMLRepository:
    """Репозиторий для сериализации в формат XML."""

    def __init__(self, file_path):
        self.file_path = file_path

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': str(object_id)})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = str(value)

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')

    def save(self, user):
        self.start_object('user', user.user_id)
        self.add_property('username', user.username)
        self.add_property('profile', user.profile)
        self.add_property('likes', str(user.likes))
        with open(self.file_path, 'wb') as file:
            file.write(self.to_str().encode())

class ObjectSerializer:
    """Сериализатор объектов."""

    def __init__(self, factory):
        self.factory = factory

    def serialize(self, serializable, format):
        repository = self.factory.create_repository(format)
        serializable.serialize(repository)
        return repository.to_str()
class RepositoryFactory:
    """Фабрика репозиториев."""

    def create_repository(self, format, file_path=None, connection_string=None):
        if format == 'JSON':
            return self.create_json_repository(file_path)
        elif format == 'XML':
            return self.create_xml_repository(file_path)
        elif format == 'Relational':
            return self.create_relational_repository(connection_string)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def create_json_repository(self, file_path):
        return JSONRepository(file_path)

    def create_xml_repository(self, file_path):
        return XMLRepository(file_path)

    def create_relational_repository(self, connection_string):
        return RelationalRepository(connection_string)



