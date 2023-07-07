class BankAccount:
    def __init__(self, account_number, password):
        self.account_number = account_number
        self.password = password
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully. Current balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Account balance: {self.balance}")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

    def login(self):
        entered_account_number = input("Enter account number: ")
        entered_password = input("Enter password: ")

        if entered_account_number == self.account_number and entered_password == self.password:
            print("Login successful.")
            return True

        print("Invalid account number or password.")
        return False


# Example usage
account = BankAccount("1234", "1234")

while True:
    print("Welcome to the ATM!")
    if account.login():
        while True:
            print("\nSelect an option:")
            print("1. Check Balance")
            print("2. Deposit Amount")
            print("3. Withdraw Amount")
            print("4. Display Account Details")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "4":
                account.display_details()
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please try again.")
    else:
        retry = input("Do you want to retry? (yes/no): ")
        if retry.lower() != "yes":
            print("Thank you for using the ATM. Goodbye!")
            break
