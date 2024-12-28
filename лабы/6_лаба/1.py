class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        if self.__password == password:
            return True
        return False

Vasya = UserAccount("Vasya_Petrov", "vasyundra_2006@gamil.com", "123456")
print(Vasya.check_password('123456'))
Vasya.set_password("qwerty")
print(Vasya.check_password('123456'))
print(Vasya.check_password('qwerty'))
print(Vasya.__password)

