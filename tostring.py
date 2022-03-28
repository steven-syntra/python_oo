class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)
        return s

    # Add the __repr__method
    def __repr__(self):
        return "Employee(\"{}\", {})".format(self.name, self.salary)


emp1 = Employee("Amar Howard", 30000)
mynstring = "Het begin er van en " + str(emp1)
print(mynstring)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)