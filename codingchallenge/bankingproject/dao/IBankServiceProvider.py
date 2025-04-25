from abc import ABC, abstractmethod
from entity.Customer import Customer

class IBankServiceProvider(ABC):

    @abstractmethod
    def create_account(self, customer: Customer, acc_no: int, acc_type: str, balance: float):
        pass

    @abstractmethod
    def listAccounts(self):
        pass

    @abstractmethod
    def calculateInterest(self):
        pass
