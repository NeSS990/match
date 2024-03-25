from Classes.User import User
from Classes.Profile import Profile
from Classes.Gift import Gift
from Classes.Chat import Chat
from Repositories.UserRespository import UserRepository
from Repositories.ChatRepository import ChatRepository
from Repositories.GiftRepository import GiftRepository

# Создаем фейковый репозиторий
user_repository = UserRepository()
chat_repository = ChatRepository()
gift_repository = GiftRepository()

# Пример использования
user1 = User(user_id=1, username="user1")
profile1 = Profile(profile_id=1, user_id=user1.user_id, bio="Hello, I'm user1!")
user_repository.save_user(user1)

chat1 = Chat(chat_id=1, user_id=user1.user_id)
chat_repository.save_chat(chat1)

gift1 = Gift(gift_id=1, name="Teddy Bear", price=20)
gift_repository.save_gift(gift1)

# Пример получения пользователя и его чата из репозитория
retrieved_user = user_repository.find_user_by_id(1)
retrieved_chat = chat_repository.find_chat_by_id(1)

# Выводим информацию
print(f"User: {retrieved_user.username}, Profile: {retrieved_user.profile.bio}")
print(f"Chat ID: {retrieved_chat.chat_id}, User ID: {retrieved_chat.user_id}")
