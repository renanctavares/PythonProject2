

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

    def __check_limit(self, checking_value):
        available_value = self.__balance + self.__limit
        return checking_value <= available_value

    def withdraw(self, value):
        if(self.__check_limit(value)):
            self.__balance -= value
            print("{}, your new balance is {}".format(self.__holder, self.__balance))
        else:
            print("The value {} is over your limit".format(value))

    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)

    def get_balance(self):
        return self.__balance

    def get_holder(self):
        return self.__holder

    @property
    def limit(self):
        print("Property")
        return self.__limit

    @limit.setter
    def limit(self, limit):
        print("Setter")
        self.__limit = limit
