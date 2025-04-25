import sqlite3

def initialize_database():
    conn = sqlite3.connect("HMBank.db")
    cursor = conn.cursor()

    # Create Customers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            DOB DATE,
            email TEXT UNIQUE NOT NULL,
            phone_number TEXT,
            address TEXT
        );
    """)

    # Create Accounts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            account_type TEXT CHECK(account_type IN ('savings', 'current', 'zero_balance')),
            balance REAL DEFAULT 0.0,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
        );
    """)

    # Create Transactions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,
            transaction_type TEXT CHECK(transaction_type IN ('deposit', 'withdrawal', 'transfer')),
            amount REAL NOT NULL,
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
        );
    """)

    conn.commit()
    conn.close()
    print("✅ Tables created successfully without using SQL file.")

if __name__ == "__main__":
    initialize_database()
