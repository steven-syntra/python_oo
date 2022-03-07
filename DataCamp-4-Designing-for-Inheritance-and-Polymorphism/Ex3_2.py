# Create a Customer class
class Customer:

    def __init__(self, name, new_bal):
        self.name = name

        if new_bal < 0:
            raise ValueError
        else:
            self._balance = new_bal

