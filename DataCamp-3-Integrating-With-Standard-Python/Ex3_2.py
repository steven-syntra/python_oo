# Define SalaryError inherited from ValueError
class SalaryError(ValueError):
    pass


# Define BonusError inherited from SalaryError
class BonusError(SalaryError):
    pass
