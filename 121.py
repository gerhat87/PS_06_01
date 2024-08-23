class user_Manager():
    def __init__(self, user):
        self.user = user
    def change_user_name(self, user_name):
        self.user_name = user_name

    def save_user_name(self):
        file = open('user_name.txt', 'w')
        file.write(self.user_name)
        file.close()

class User():
    def __init__(self, user):
        self.user = user

class UcerNameChanger():
    def change_user_name(self, user):
        self.user = user
    def change_name(self, new_name):
        self.new_name = new_name

class SaveUser
    def __init__(self, user):
        self.user = user
    def save_user(self):
        file = open('user_name.txt', 'w')
        file.write(self.user)
        file.close()
