from Ex3_4 import Employee, BonusError, SalaryError

emp = Employee("Katze Rik", 50000)

try:
    emp.give_bonus(7000)
except BonusError:
    print("BonusError caught")
except SalaryError:
    print("SalaryError caught")
