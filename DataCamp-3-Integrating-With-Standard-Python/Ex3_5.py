from Ex3_4 import Employee, BonusError, SalaryError

emp = Employee("Katze Rik", salary=50000)

try:
    emp.give_bonus(7000)
except SalaryError:
    print("SalaryError caught!")

try:
    emp.give_bonus(7000)
except BonusError:
    print("BonusError caught!")

try:
    emp.give_bonus(-100000)
except SalaryError:
    print("SalaryError caught again!")

try:
    emp.give_bonus(-100000)
except BonusError:
    print("BonusError caught again!")


