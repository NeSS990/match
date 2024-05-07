from Repositories.Repositories import JSONRepositoryFactory, RelationalRepositoryFactory, XMLRepositoryFactory


def create_user(repository):
    user_id = int(input("Введите ID пользователя: "))
    username = input("Введите имя пользователя: ")
    profile = input("Введите профиль пользователя: ")
    age = int(input("Введите возраст пользователя: "))

    user_data = {
        "user_id": user_id,
        "username": username,
        "profile": profile,
        "age": age
    }

    repository.save(user_data)
    print("Пользователь успешно создан.")

def login_as_user(repository):
    user_id = int(input("Введите ID пользователя: "))

    users = repository.find_users()
    for user in users:
        if user["user_id"] == user_id:
            print(f"ID: {user['user_id']}")
            print(f"Имя: {user['username']}")
            print(f"Профиль: {user['profile']}")
            print(f"Возраст: {user['age']}")
            like = input("Поставить лайк (y/n)? ").lower()
            if like == 'y':
                # Ваш код для постановки лайка
                pass
            else:
                print("Лайк не поставлен.")
            break
    else:
        print("Пользователь с указанным ID не найден.")

def main_menu(repository):
    while True:
        print("Меню:")
        print("1) Создать пользователя")
        print("2) Зайти под пользователем")
        print("3) Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == '1':
            create_user(repository)
        elif choice == '2':
            login_as_user(repository)
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    print("Выберите тип репозитория:")
    print("1) XML")
    print("2) JSON")
    print("3) Реляционный")
    
    repository_choice = input("Ваш выбор: ")
    if repository_choice == '1':
        repository_factory = XMLRepositoryFactory("users.xml")
    elif repository_choice == '2':
        repository_factory = JSONRepositoryFactory("users.json")
    elif repository_choice == '3':
        repository_factory = RelationalRepositoryFactory("connection_string")
    else:
        print("Некорректный выбор репозитория.")
        exit()

    repository = repository_factory.create_repository()
    main_menu(repository)
