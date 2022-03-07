# class Customer:
#
#     def identify(self, name):
#         print("I am Customer " + name)
#
#
# cust = Customer()
# cust.identify("Laura")

# class Customer:
#
#     def set_name(self, name):
#         self.name = name
#
#     def identify(self):
#         print("I am Customer " + self.name)
#
#
# cust = Customer()
# cust.set_name("Laura")
# cust.identify()

# class Customer:
#
#     def __init__(self, name):
#         self.name = name
#         print("The __init__ method was called")
#
#
# cust = Customer("Laura")
# print(cust.name)

class Customer:

    """
    Dit is een docstring, documentatie over de Customer class
    """
    # balance has default value 0
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print("The __init__ method was called")


cust = Customer("Laura")
print(cust.name)
print(cust.balance)
