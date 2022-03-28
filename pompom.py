import datetime


class Voertuig:
    def __eq__(self, other):

        if isinstance(other, datetime.datetime):
            print("Datetimes zijn altijd gelijk aan Parents!")
            return True

        print("Voertuig's __eq__() called")
        print(f"self is a {type(self)}")
        print(f"other is a {type(other)}")

        if type(self) == type(other):
            return True
        else:
            return False


class Auto(Voertuig):
    def __eq__(self, other):
        print("Auto's __eq__() called")
        print(f"self is a {type(self)}")
        print(f"other is a {type(other)}")

        if type(self) == type(other):
            return True
        else:
            return False


class Zoogdier():
    pass
    # def __eq__(self, other):
    #     print("Zoogdier's __eq__() called")
    #     print(f"self is a {type(self)}")
    #     print(f"other is a {type(other)}")
    #
    #     if type(self) == type(other):
    #         return True
    #     else:
    #         return False


z = Zoogdier()
v = Voertuig()

print("Zoogdier == Voertuig:", z == v)
print("Voertuig == Zoogdier:", v == z)
print("Zoogdier", z)
print("Voertuig", v)

# p = Parent()
# p1 = Parent()
# p2 = Parent()
# c = Child()
#
# datetime_object = datetime.datetime.now()
# print(datetime_object)
#
# print(p1 == p2)
# print(c == p)
# print(p == c)
# print("=====datetime experiment======")
# print(datetime_object == p)
# print(p == datetime_object)


