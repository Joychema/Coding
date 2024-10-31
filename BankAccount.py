#bank account system
from html.parser import interesting_normal


class BankAccount():
    def __init__(self, account_number, balance=0):
        self.account_number=account_number
        self.balance=balance

    def deposit(self, amount):
        self.balance +=amount
        return f"Ksh.{amount} deposited. Account Balance:{self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate=interest_rate

    def apply_interest(self):
        self.balance * self.interest_rate
        self.balance += self.balance * self.interest_rate
        return f"Interest applied. New Balance: Ksh {self.balance}"

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0,overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit=overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            return f"Ksh {amount} withdrawn. Account Balance: {self.balance}"
        else:
            return f"Withdrawal denied, overdraft limit exceeded. "

bankaccount = BankAccount(911525709)
savings = SavingsAccount(911525709, balance=100)
remains = CheckingAccount(911525709, balance=100)

print(bankaccount.deposit(100))
print(savings.apply_interest())
print(remains.withdraw(50))
