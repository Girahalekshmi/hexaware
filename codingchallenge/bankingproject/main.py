import sqlite3
from entity.Customer import Customer
from entity.Account import Account

def list_tables():
    # Establish database connection
    conn = sqlite3.connect("HMBank.db")
    cursor = conn.cursor()

    # List all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("\n Tables in Database:")
    for table in tables:
        print(table[0])

    conn.close()

def view_table_data(table_name):
    # Establish database connection
    conn = sqlite3.connect("HMBank.db")
    cursor = conn.cursor()

    # Fetch all data from the given table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    print(f"\n Data from {table_name} table:")
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    # List all tables in the database
    list_tables()

    # View data from all tables (you can specify the table names if needed)
    list_of_tables = ['Customers', 'Accounts','Transactions']

    for table in list_of_tables:
        view_table_data(table)


customer1 = Customer(112, "giraha", "lekshmi", "1990-04-24", "giraha@gmail.com", "9876543210", "123 Elm St")

# Create a savings account for giraha
account1 = Account(1001, "savings", 5000.0)

# Interact with the account
account1.deposit(2000)
account1.withdraw(1000)
interest = account1.calculate_interest()

# Print the account balance and interest
print(f"Updated Balance: {account1.get_balance()}")
print(f"Interest: {interest}")

