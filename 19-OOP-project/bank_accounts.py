class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposited {amount} into your account.\n{self.name} has a new balance of ${self.balance}")

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account {self.name} only has a balance of {self.balance:.2f}")

    def withdraw_example(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print(f"\nWithdraw complete")
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")



    def withdraw(self, amount):
        if self.balance < amount:
            return print(f"\nUnable to withdraw {amount}.\nAccount: {self.name} has a balance of ${self.balance}.\nYou are trying to withdraw -${amount - self.balance} more than you have.")
        else:
            self.balance = self.balance - amount
            print(f"\nYou withdrew ${amount}. Account '{self.name}' has a remaining balance of ${self.balance}.")
            return

    def transfer(self, amount, account):
        try:
            print(f"\nInitiating transfer.....\n")
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            account.deposit(amount)
            print(f"\nTransfer complete")
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

class InterestRewardsAcct(BankAccount):
    def int_deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")