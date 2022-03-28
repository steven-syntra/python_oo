class Customer:

    # balance has default value 0
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.telefoon = None

        print("The __init__ method was called")


cust = Customer("Laura")
print(cust.name)
print(cust.balance)
print(cust.telefoon)
