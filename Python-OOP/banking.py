from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):
    @abstractmethod
    def create_account(self, name, initial_amount):
        return 0

    @abstractmethod
    def authenticate(self, name, account_number):
        return 0

    @abstractmethod
    def deposit(self, deposit_amount):
        return 0

    @abstractmethod
    def withdraw(self, withdrawal_amount):
        return 0

    @abstractmethod
    def display_balance(self):
        return 0


class SavingsAcount(Account):
    def __init__(self):
        self.savings_accounts = {}

    def create_account(self, name, initial_deposit):
        self.account_number = randint(1000, 99999)
        self.savings_accounts[self.account_number] = [name, initial_deposit]
        print("Account creation is successful. Your account number is", self.account_number)

    def authenticate(self, name, account_number):
        if account_number in self.savings_accounts.keys():
            if self.savings_accounts[account_number][0] == name:
                print("Authentication Successful")
                self.account_number = account_number
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def deposit(self, deposit_amount):
        self.savings_accounts[self.account_number][1] += deposit_amount
        print("Depsoit was successful.")
        self.display_balance()

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.savings_accounts[self.account_number][1]:
            print("Insufficient balance")
        else:
            self.savings_accounts[self.account_number][1] -= withdrawal_amount
            print("Withdrawal was successful.")
            self.display_balance()

    def display_balance(self):
        print("Available balance:", self.savings_accounts[self.account_number][1])


savings_account = SavingsAcount()
while True:
    print()
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    users_choice = int(input())
    print()
    if users_choice is 1:
        print()
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposit: ")
        deposit = int(input())
        savings_account.create_account(name, deposit)
        print()
    elif users_choice is 2:
        print()
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authentication_state = savings_account.authenticate(name, accountNumber)
        print()
        if authentication_state is True:
            while True:
                print()
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display avialable balance")
                print("Enter 4 to go back to the previous menu")
                users_choice = int(input())
                print()
                if users_choice is 1:
                    print()
                    print("Enter a withdrawal amount")
                    withdrawal_amount = int(input())
                    savings_account.withdraw(withdrawal_amount)
                    print()
                elif users_choice is 2:
                    print()
                    print("Enter an amount to be deposited")
                    deposit_amount = int(input())
                    savings_account.deposit(deposit_amount)
                    print()
                elif users_choice is 3:
                    print()
                    savings_account.display_balance()
                    print()
                elif users_choice is 4:
                    break
    elif users_choice is 3:
        quit()
