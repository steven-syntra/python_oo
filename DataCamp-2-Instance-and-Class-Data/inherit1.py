class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print(self):
        print(self.firstname, self.lastname)


class Student(Person):

    def __init__(self, fname, lname, leerjaar):
        super().__init__(fname, lname)
        self.leerjaar = leerjaar

    def print(self):
        print(self.firstname, self.lastname, self.leerjaar)

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.leerjaar)


# Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.print()

x = Student("Mike", "Olsen", 2022)
x.print()
x.welcome()
