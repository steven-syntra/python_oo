class BankAccount:
    # MODIFY to initialize a number attribute
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount

    # Define __eq__ that returns True if the number attributes are equal
    def __eq__(self, other):
        return self.number == other.number


# Create accounts and compare them
acct1 = BankAccount('BE12345', 1000)
acct2 = BankAccount('BE12345', 1000)
acct3 = BankAccount('NL45678', 1000)
print(acct1 == acct2)
print(acct1 == acct3)


class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance

    def withdraw(self, amount):
        self.balance -= amount

        # MODIFY to add a check for the type()

    def __eq__(self, other):
        print(f"Comparing {self.number} and {other.number}")
        return (self.number == other.number) and isinstance(other, BankAccount)


acct = BankAccount(873555333)
acct2 = BankAccount(873555333)
pn = Phone(873555333)
pn2 = Phone(873555333)
print(acct == pn)
print(acct == acct2)
print(pn == pn2)
