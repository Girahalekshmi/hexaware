from entity.Customer import Customer



class Account:
    def __init__(self, account_id=None, customer_id=None, account_type="savings", balance=0.0):
        self.__account_id = account_id
        self.__customer_id = customer_id
        self.__account_type = account_type
        self.__balance = balance

    # Getters
    def get_account_id(self):
        return self.__account_id

    def get_customer_id(self):
        return self.__customer_id

    def get_account_type(self):
        return self.__account_type

    def get_balance(self):
        return self.__balance

    # Setters
    def set_account_id(self, account_id):
        self.__account_id = account_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def set_balance(self, balance):
        self.__balance = balance

    # Methods
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def calculate_interest(self):
        if self.__account_type == "savings":
            interest_rate = 0.045  # 4.5%
            return self.__balance * interest_rate
        return 0.0

    def __str__(self):
        return f"Account ID: {self.__account_id}, Type: {self.__account_type}, Balance: ₹{self.__balance:.2f}"

customer1 = Customer(112, "giraha", "lekshmi", "1990-04-24", "giraha@gmail.com", "9876543210", "123 Elm St")

# Create a savings account for giraha with the customer_id from the created customer
account1 = Account(1001, customer1.get_customer_id(), "savings", 5000.0)

# Interact with the account
account1.deposit(2000)  # Deposit 2000
account1.withdraw(1000)  # Withdraw 1000
interest = account1.calculate_interest()  # Calculate interest

# Print the account balance and interest
print(f"Updated Balance: ₹{account1.get_balance():.2f}")
print(f"Interest: ₹{interest:.2f}")
