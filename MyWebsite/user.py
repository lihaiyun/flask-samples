class User:
    dict = {}

    def __init__(self, username, password, name, email):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__email = email

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    @staticmethod
    def get_dict():
        dict = User.dict
        if len(dict) == 0:
            user1 = User('haiyun', 'password', 'Haiyun', 'hy@gmail.com')
            dict[user1.get_username()] = user1
            user2 = User('alex', 'password123', 'Alex', 'alex@gmail.com')
            dict[user2.get_username()] = user2
        return dict

    @staticmethod
    def get_user(username):
        dict = User.get_dict()
        user = dict.get(username)
        return user

    @staticmethod
    def authenticate(username, password):
        user = User.get_user(username)
        if user is not None:
            if user.get_password() == password:
                return True
        return False
