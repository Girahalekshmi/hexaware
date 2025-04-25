import sqlite3
from dao.ICustomerServiceProvider import ICustomerServiceProvider
from dao.IBankServiceProvider import IBankServiceProvider
from entity.Customer import Customer
from entity.Account import Account
from exception.InvalidAccountException import InvalidAccountException
from exception.InsufficientFundException import InsufficientFundException
from exception.OverDraftLimitExceededException import OverDraftLimitExceededException
from util.DBConnUtil import get_connection


class BankServiceProviderImpl(ICustomerServiceProvider, IBankServiceProvider):
    def __init__(self):
        pass

    def create_account(self, customer: Customer, acc_no: int, acc_type: str, balance: float):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Customers (customer_id, first_name, last_name, DOB, email, phone_number, address)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (customer.customer_id, customer.first_name, customer.last_name, customer.dob,
                  customer.email, customer.phone_number, customer.address))

            cursor.execute("""
                INSERT INTO Accounts (account_id, customer_id, account_type, balance)
                VALUES (?, ?, ?, ?)
            """, (acc_no, customer.customer_id, acc_type, balance))

            conn.commit()
            print(f"Account {acc_no} for {customer.first_name} created successfully!")

        except sqlite3.Error as e:
            print("Error in create_account():", e)

        finally:
            conn.close()

    def deposit(self, account_number: int, amount: float):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Accounts SET balance = balance + ? WHERE account_id = ?
            """, (amount, account_number))

            if cursor.rowcount == 0:
                raise InvalidAccountException()

            conn.commit()
            print(f"Deposited ₹{amount} to Account {account_number}")

        except sqlite3.Error as e:
            print("Error in deposit():", e)

        finally:
            conn.close()

    def withdraw(self, account_number: int, amount: float):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT balance FROM Accounts WHERE account_id = ?
            """, (account_number,))
            result = cursor.fetchone()

            if not result:
                raise InvalidAccountException()

            balance = result[0]
            if balance < amount:
                raise InsufficientFundException()

            cursor.execute("""
                UPDATE Accounts SET balance = balance - ? WHERE account_id = ?
            """, (amount, account_number))

            conn.commit()
            print(f"Withdrew ₹{amount} from Account {account_number}")

        except (InvalidAccountException, InsufficientFundException) as e:
            print("Error:", e)

        except sqlite3.Error as e:
            print("Database Error in withdraw():", e)

        finally:
            conn.close()

    def get_account_balance(self, account_number: int):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT balance FROM Accounts WHERE account_id = ?
            """, (account_number,))
            result = cursor.fetchone()

            if not result:
                raise InvalidAccountException()

            print(f"Balance for Account {account_number} is ₹{result[0]}")
            return result[0]

        except InvalidAccountException as e:
            print("Error:", e)

        finally:
            conn.close()

    def getAccountDetails(self, account_number: int):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT c.first_name, c.last_name, c.email, a.account_type, a.balance
                FROM Customers c
                JOIN Accounts a ON c.customer_id = a.customer_id
                WHERE a.account_id = ?
            """, (account_number,))
            result = cursor.fetchone()

            if not result:
                raise InvalidAccountException()

            print("Account Details:")
            print("Customer Name:", result[0], result[1])
            print("Email:", result[2])
            print("Account Type:", result[3])
            print("Balance:", result[4])

        except InvalidAccountException as e:
            print("Error:", e)

        finally:
            conn.close()

    def listAccounts(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Accounts")
            accounts = cursor.fetchall()

            print("All Bank Accounts:")
            for acc in accounts:
                print(acc)

        except sqlite3.Error as e:
            print("Error fetching account list:", e)

        finally:
            conn.close()

    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT balance FROM Accounts WHERE account_id = ?", (from_account_number,))
            from_result = cursor.fetchone()
            if not from_result:
                raise InvalidAccountException("From account not found")
            if from_result[0] < amount:
                raise InsufficientFundException()

            cursor.execute("SELECT balance FROM Accounts WHERE account_id = ?", (to_account_number,))
            to_result = cursor.fetchone()
            if not to_result:
                raise InvalidAccountException("To account not found")

            cursor.execute("UPDATE Accounts SET balance = balance - ? WHERE account_id = ?", (amount, from_account_number))
            cursor.execute("UPDATE Accounts SET balance = balance + ? WHERE account_id = ?", (amount, to_account_number))

            conn.commit()
            print(f"Transferred ₹{amount} from {from_account_number} to {to_account_number}")

        except (InvalidAccountException, InsufficientFundException) as e:
            print("Error:", e)

        finally:
            conn.close()

    def calculateInterest(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            interest_rate = 4.5 / 100
            cursor.execute("""
                SELECT account_id, balance FROM Accounts WHERE account_type = 'savings'
            """)
            savings_accounts = cursor.fetchall()

            for account in savings_accounts:
                interest = account[1] * interest_rate
                new_balance = account[1] + interest
                cursor.execute("""
                    UPDATE Accounts SET balance = ? WHERE account_id = ?
                """, (new_balance, account[0]))

            conn.commit()
            print("Interest calculated and added to all savings accounts.")

        except sqlite3.Error as e:
            print("Error in calculateInterest():", e)

        finally:
            conn.close()
