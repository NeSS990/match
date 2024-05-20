from Classes.Classes import User
from Repositories.Repositories import RepositoryFactory, ObjectSerializer

def main():
    # Создаем фабрику репозиториев
    repository_factory = RepositoryFactory()
    connection_string = None
    file_path = None
    # Создаем объект сериализатора
    object_serializer = ObjectSerializer(repository_factory)

    # Предлагаем пользователю выбрать формат для сериализации
    print("Выберите формат для сериализации:")
    print("1) JSON")
    print("2) XML")
    print("3) Реляционная база данных")
    choice = input("Ваш выбор: ")

    # Проверяем выбор пользователя и выбираем соответствующий формат
    if choice == '1':
        format = 'JSON'
        file_path = 'users.json'  # Файл JSON для сохранения пользователей
    elif choice == '2':
        format = 'XML'
        file_path = 'users.xml'  # Файл XML для сохранения пользователей
    elif choice == '3':
        format = 'Relational'
        connection_string = {
            'host': 'localhost',
            'database': 'match',
            'user': 'root',
            'password': ''
        }
    else:
        print("Некорректный ввод.")
        return

    # Создаем репозиторий пользователей
    repository = repository_factory.create_repository(format, file_path=file_path, connection_string=connection_string)

    # Создаем пользователя
    user = User(user_id=1, username="JohnDoe", profile="Some profile", likes=[2, 3, 4])

    # Сериализуем и сохраняем пользователя
    object_serializer.serialize(user, format)
    repository.save(user)

if __name__ == "__main__":
    main()
