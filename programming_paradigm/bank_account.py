# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional initial balance.
        :param initial_balance: Starting balance for the account (default is 0).
        """
        self._account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """
        Deposit a specified amount to the account balance.
        :param amount: Amount to deposit.
        """
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account balance if sufficient funds are available.
        :param amount: Amount to withdraw.
        :return: True if withdrawal is successful, False otherwise.
        """
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")