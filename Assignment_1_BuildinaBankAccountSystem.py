"""
Bank Account Management System
This program demonstrates object-oriented programming concepts
such as classes, objects, encapsulation, and methods.
"""


class BankAccount:
    """
    A class to represent a bank account.
    """

    _account_counter = 1000  # Class variable for auto account number generation

    def __init__(self, account_holder, initial_balance=0.0):
        """
        Initializes a new bank account.
        """
        BankAccount._account_counter += 1
        self.__account_number = BankAccount._account_counter
        self.__account_holder = account_holder
        self.__balance = float(initial_balance)

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful: ₹{amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds exist.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance. Withdrawal failed.")
        else:
            self.__balance -= amount
            print(f"Withdrawal successful: ₹{amount:.2f}")

    def display_details(self):
        """
        Displays account details.
        """
        print("Account Holder:", self.__account_holder)
        print("Account Number:", self.__account_number)
        print(f"Current Balance: ₹{self.__balance:.2f}")
        print("-" * 40)


# Testing the BankAccount class
account_1 = BankAccount("Rama Krushna Pati", 5000)
account_2 = BankAccount("Anita Sharma", 3000)

account_1.deposit(1500)
account_1.withdraw(2000)
account_1.display_details()

account_2.deposit(1000)
account_2.withdraw(5000)
account_2.display_details()
