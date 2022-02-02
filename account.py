

class Account:

    def __init__(self, number, holder, balance, limit):
        print("Constructing object...")
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def account_balance(self):
        print("{}, your account balance is {}".format(self.__holder, self.__balance))

    def deposit(self, value):
        self.__balance += value
        print("{}, your new balance is {}".format(self.__holder, self.__balance))

    def withdraw(self, value):
        self.__balance -= value
        print("{}, your new balance is {}".format(self.__holder, self.__balance))

    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)

    def get_balance(self):
        return self.__balance

    def get_holder(self):
        return self.__holder

    def get_limit(self):
        return self.__limit

    def set_limit(self, limit):
        self.__limit = limit
