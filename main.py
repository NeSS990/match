from Repositories.Repositories import XMLRepository
from lxml import etree

def save_user_to_xml(user_data):
    user_repository = XMLRepository("users.xml")
    user_repository.save(user_data)

def find_users_by_age(min_age, max_age):
    user_repository = XMLRepository("users.xml")
    query = f"//item[age>={min_age} and age<={max_age}]"
    users = user_repository.find(query)
    return users

if __name__ == "__main__":
    # Сохранение пользователя в XML
    user_data = {
        "user_id": 2,
        "username": "Artem",
        "profile": "I love hiking and traveling!",
        "age": 10
    }
    save_user_to_xml(user_data)

    # Поиск пользователей по возрасту
    min_age = 25
    max_age = 35
    users = find_users_by_age(min_age, max_age)
    print("Users aged between", min_age, "and", max_age, ":")
    for user in users:
        username = user.find("username").text
        print(username)
