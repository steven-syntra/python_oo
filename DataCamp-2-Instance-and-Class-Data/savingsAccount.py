from bankAccount import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        BankAccount.__init__(self, balance)
        self.interest_rate = interest_rate


acct = SavingsAccount(1000, 0.03)
print(acct.interest_rate)
