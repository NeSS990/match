# user_repository.py
class UserRepository:
    def __init__(self):
        self.users = []

    def save_user(self, user):
        self.users.append(user)

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
