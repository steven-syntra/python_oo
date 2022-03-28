class Parent():

    def vermenigvuldig(self, getal):
        return getal * 2        # returnt int


class Child(Parent):

    # 2de parameter moet optioneel zijn voor LSP
    def vermenigvuldig(self, getal, factor=4):
        return getal * factor        # returnt int

    def maal10(self, getal):
        return getal * 10


p = Parent()
c = Child()

print(c.vermenigvuldig(8))       # hier moet je ook c.vermenigvuldig() kunnen schrijven
print(c.vermenigvuldig(8,2))
print(c.maal10(8))

