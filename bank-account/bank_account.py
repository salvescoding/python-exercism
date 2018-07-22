from threading import RLock


class BankAccount(object):

    def __init__(self):
        self._balance = None
        self._lock = RLock()

    def error_if_closed(self) -> None:
        """
        Raise a ValueError if the account is already closed.
        """
        if self._balance is None:
            raise ValueError("Cannot perform operations on a closed account!")

    def get_balance(self) -> int:
        """
        Returns the balance
        """
        with self._lock:
            self.error_if_closed()
            return self._balance

    def open(self):
        """
        Opens the account and the set balance to 0
        """
        with self._lock:
            self._balance = 0

    def deposit(self, amount: int):
        """
        Deposits the money into the acccount if not closed and amount is positive
        """
        with self._lock:
            self.error_if_closed()
            if amount < 0:
                raise ValueError("Amount needs to be bigger than 0")
            self._balance += amount

    def withdraw(self, amount: int):
        """
        Withdraw the money if account not closed and have enough money
        """
        with self._lock:
            self.error_if_closed()
            if amount > self._balance:
                raise ValueError("Insufecient funds")
            elif amount <= 0:
                raise ValueError("Amount have to be bigger than 0")
            self._balance -= amount

    def close(self):
        with self._lock:
            self._balance = None


