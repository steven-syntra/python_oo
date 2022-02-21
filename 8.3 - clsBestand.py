import datetime


class Bestand:

    def __init__(self, naam, extensie ):
        self.naam = naam
        self.extensie = extensie
        self.fullname = naam + "." + extensie
        self.creatie = datetime.datetime.now()

    def Opslaan(self):
        fp = open(self.fullname, "w")
        fp.write(self.inhoud)
        fp.close()
        print("Bestand %s opgeslagen" % self.fullname)

    def Dupliceer(self):
        naam_kopie = self.naam + "_kopie" + "." + self.extensie
        fp = open(naam_kopie, "w")
        fp.write(self.inhoud)
        fp.close()
        print("Bestand %s opgeslagen" % naam_kopie)

    def Info(self):
        print("Fullname: %s" % self.fullname)
        print("Gecreëerd op: %s" % self.creatie)
        print("Inhoud: %s tekens" % len(self.inhoud))


b1 = Bestand("mijnbestand", "txt")
b1.inhoud = "Pompom Tralala Bom Bom"
b1.Opslaan()
b1.Dupliceer()
b1.Info()

