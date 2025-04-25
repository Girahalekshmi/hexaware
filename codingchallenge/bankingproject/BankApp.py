from dao.BankServiceProviderImpl import BankServiceProviderImpl
from entity.Customer import Customer

def main():
    bank = BankServiceProviderImpl()

    while True:
        print("\n====== HM BANK SYSTEM ======")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Get Account Balance")
        print("6. Get Account Details")
        print("7. List All Accounts")
        print("8. Calculate Interest (Savings Only)")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        try:
            if choice == '1':
                # Create account
                customer_id = int(input("Enter Customer ID: "))
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                email = input("Email: ")
                phone = input("Phone Number: ")
                address = input("Address: ")

                acc_no = int(input("Account Number: "))
                acc_type = input("Account Type (savings/current): ").lower()
                balance = float(input("Initial Deposit: "))

                customer = Customer(customer_id, first_name, last_name, dob, email, phone, address)
                bank.create_account(customer, acc_no, acc_type, balance)

            elif choice == '2':
                acc_no = int(input("Account Number: "))
                amount = float(input("Amount to Deposit: "))
                bank.deposit(acc_no, amount)

            elif choice == '3':
                acc_no = int(input("Account Number: "))
                amount = float(input("Amount to Withdraw: "))
                bank.withdraw(acc_no, amount)

            elif choice == '4':
                from_acc = int(input("From Account: "))
                to_acc = int(input("To Account: "))
                amount = float(input("Amount to Transfer: "))
                bank.transfer(from_acc, to_acc, amount)

            elif choice == '5':
                acc_no = int(input("Account Number: "))
                bank.get_account_balance(acc_no)

            elif choice == '6':
                acc_no = int(input("Account Number: "))
                bank.getAccountDetails(acc_no)

            elif choice == '7':
                bank.listAccounts()

            elif choice == '8':
                bank.calculateInterest()

            elif choice == '9':
                print("Thank you for using HM Bank. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 9.")

        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()
