from datetime import datetime

class Transaction:
    def __init__(self, transaction_id=None, account_id=None, transaction_type="", amount=0.0, transaction_date=None):
        self.__transaction_id = transaction_id
        self.__account_id = account_id
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__transaction_date = transaction_date if transaction_date else datetime.now()

    # Getters
    def get_transaction_id(self):
        return self.__transaction_id

    def get_account_id(self):
        return self.__account_id

    def get_transaction_type(self):
        return self.__transaction_type

    def get_amount(self):
        return self.__amount

    def get_transaction_date(self):
        return self.__transaction_date

    # Setters
    def set_transaction_id(self, transaction_id):
        self.__transaction_id = transaction_id

    def set_account_id(self, account_id):
        self.__account_id = account_id

    def set_transaction_type(self, transaction_type):
        self.__transaction_type = transaction_type

    def set_amount(self, amount):
        self.__amount = amount

    def set_transaction_date(self, transaction_date):
        self.__transaction_date = transaction_date

    def __str__(self):
        return f"{self.__transaction_date.strftime('%Y-%m-%d %H:%M:%S')} | {self.__transaction_type.title()} ₹{self.__amount:.2f}"

transaction1 = Transaction(transaction_id=1, account_id=101, transaction_type="deposit", amount=1000.0)

# Print transaction details
print("Transaction 1 Details:", transaction1)

# Set new amount and transaction type
transaction1.set_amount(2000.0)
transaction1.set_transaction_type("withdrawal")

# Print updated transaction details
print("Updated Transaction 1 Details:", transaction1)

# Create another transaction with a custom date
transaction2 = Transaction(transaction_id=2, account_id=102, transaction_type="deposit", amount=1500.0, transaction_date=datetime(2025, 4, 24, 15, 30, 0))

# Print details of the second transaction
print("Transaction 2 Details:", transaction2)