class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0.0):
      
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
       
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    
    def display_account_details(self):
     
        print(f"\nAccount Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")



account_number = input("Enter account number: ")
name = input("Enter account holder name: ")
account_type = input("Enter account type (e.g., Savings, Checking): ")
initial_balance = float(input("Enter initial balance (default is 0.0): "))


account = BankAccount(account_number, name, account_type, initial_balance)


account.display_account_details()

while True:
    print("\nMenu:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Display Account Details")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
   
        deposit_amount = float(input("Enter amount to deposit: "))
        account.deposit(deposit_amount)

    elif choice == '2':
     
        withdraw_amount = float(input("Enter amount to withdraw: "))
        account.withdraw(withdraw_amount)

    elif choice == '3':
     
        account.display_account_details()

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
