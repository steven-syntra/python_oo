class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance

    def withdraw(self, amount):
        self.balance -= amount

    # MODIFY to add a check for the type()
    def __eq__(self, other):
        if type(self) == type(other):
            return self.number == other.number
        else:
            return False


class Phone:
    def __init__(self, number):
        self.number = number

    # Opgelet! Type wordt niet gecontroleerd...!
    def __eq__(self, other):
        return self.number == other.number


acct = BankAccount(873555333)
pn = Phone(873555333)

print(acct == pn)
print(pn == acct)   # niet hetzelfde resultaat...!
