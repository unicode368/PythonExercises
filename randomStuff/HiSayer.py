class HiSayer:
    def __init__(self, message, name):
        self.__message = message
        self.__name = name
        self.public_var = 5

    def print_name(self):
        print(self.__message + " " + self.__name)

    def __private_name(self):
        print(self.__message + " " + self.__name)

