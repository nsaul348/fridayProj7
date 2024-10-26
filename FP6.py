# This Python program simulates a simple bank account system using a class structure, allowing a user to interactively manage their balance. The program defines a BankAccount class with attributes for an account number and a balance. It includes three methods for depositing money, withdrawing money, and checking the current balance. The main program creates an instance of the BankAccount class and uses an indefinite loop to prompt the user for their account number before each interaction. The user can then choose to deposit, withdraw, or check their balance. This program provides a basic simulation of bank account operations with an option to loop until the user exits.

class BankAccount:
    # Initialize the bank account with an account number and a starting balance
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    # Method to deposit money, increasing the balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money, decreasing the balance if funds are sufficient
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance is ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to check the current balance
    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

# Create an instance of the BankAccount class
account = BankAccount(account_number="123456")

# Main program loop to interact with the bank account
print("Welcome to the Bank Account Manager!")

while True:
    # Prompt the user for their account number to access their account
    entered_account = input("Please enter your account number (or type 'exit' to quit): ").strip()
    
    if entered_account.lower() == 'exit':
        print("Thank you for using the Bank Account Manager. Goodbye!")
        break
    
    # Check if the account number is correct
    if entered_account == account.account_number:
        print("Options: (a) Deposit Money, (b) Withdraw Money, (c) Check Balance")
        action = input("Please select an option (a/b/c): ").strip().lower()
        
        if action == 'a':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif action == 'b':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif action == 'c':
            account.check_balance()
        else:
            print("Invalid option selected. Please choose a valid option.")
    else:
        print("Account number not recognized")
