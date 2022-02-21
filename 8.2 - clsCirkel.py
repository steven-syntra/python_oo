import math

class Cirkel:

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