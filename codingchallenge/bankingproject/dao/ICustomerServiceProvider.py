from abc import ABC, abstractmethod

class ICustomerServiceProvider(ABC):

    @abstractmethod
    def get_account_balance(self, account_number: int):
        pass

    @abstractmethod
    def deposit(self, account_number: int, amount: float):
        pass

    @abstractmethod
    def withdraw(self, account_number: int, amount: float):
        pass

    @abstractmethod
    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        pass

    @abstractmethod
    def getAccountDetails(self, account_number: int):
        pass


