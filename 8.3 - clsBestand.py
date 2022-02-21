import datetime


class Bestand:

    def __init__(self, naam, extensie ):
        self.naam = naam
        self.extensie = extensie
        self.inhoud = ""
        self.fullname = naam + "." + extensie
        self.creatie = datetime.datetime.now()

    def Opslaan(self):
        self.Save(self.fullname)
        print("Bestand %s opgeslagen" % self.fullname)

    def Dupliceer(self):
        naam_kopie = self.naam + "_kopie" + "." + self.extensie
        self.Save(naam_kopie)
        print("Bestand %s opgeslagen" % naam_kopie)

    def Save(self, naam):
        with open(naam, "w") as fp:
            fp.write(self.inhoud)

    def Info(self):
        print("Fullname: %s" % self.fullname)
        print("Gecreëerd op: %s" % self.creatie)
        print("Inhoud: %s tekens" % len(self.inhoud))


b1 = Bestand("mijnbestand", "txt")
b1.inhoud = "Pompom Tralala Bom Bom"
b1.Opslaan()
b1.Dupliceer()
b1.Info()

