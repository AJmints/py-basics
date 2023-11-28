from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Alex = BankAccount(5000, "Alex")

Dave.getBalance()
Alex.getBalance()

Alex.deposit(1000)
Alex.withdraw_example(20000)
Alex.withdraw_example(100)

Alex.transfer(100, Dave)

AlexInterest = InterestRewardsAcct(1000, "Alex")

AlexInterest.getBalance()
AlexInterest.int_deposit(100)

Savings = SavingsAcct(1000, "Alex")
Savings.getBalance()
Savings.deposit(100)
Savings.transfer(10000, Dave)
Savings.transfer(100, Dave)