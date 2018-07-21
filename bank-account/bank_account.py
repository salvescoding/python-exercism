class BankAccount(object):
    def __init__(self):
        pass

    def get_balance(self):
        if not self.active:
            self.value_error()
        return self.__balance

    def open(self):
        self.active = True
        self.__balance = 0

    def deposit(self, amount):
        if not self.active or amount < 0:
            self.value_error()
        self.__balance += amount

    def withdraw(self, amount):
        if not self.active:
            self.value_error()
        if self.__balance < amount or amount < 0:
            raise ValueError
        self.__balance -= amount

    def close(self):
        self.active = False

    def value_error(self):
        raise ValueError
