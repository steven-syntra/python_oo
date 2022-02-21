import math


class Cirkel:

    straal = 0
    opp = 0
    omtrek = 0

    def __init__(self, straal):
        self.straal = straal
        self.BerekenOppervlakte()
        self.BerekenOmtrek()

    def BerekenOppervlakte(self):
        self.opp = self.straal ** 2 * math.pi

    def BerekenOmtrek(self):
        self.omtrek = self.straal * 2 * math.pi

    def Info(self):
        print("Straal: %s" % self.straal)
        print("Oppervlakte: %s" % '{0:.2f}'.format(self.opp))
        print("Omtrek: %s" % '{0:.2f}'.format(self.omtrek))


c1 = Cirkel(3)
# c1.BerekenOppervlakte()
# c1.BerekenOmtrek()
c1.Info()

c2 = Cirkel(12)
# c2.BerekenOppervlakte()
# c2.BerekenOmtrek()
c2.Info()
