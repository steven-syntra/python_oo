class Dier:
    naam = ""
    soort = ""      # hond, kat, kabeljauw
    poten = 0
    voedsel = []
    geluid = ""
    huid = ""

    # constructor
    def __init__(self, naam_dier, soort_dier):
        self.naam = naam_dier
        self.soort = soort_dier

    def beknopte_info(self):
        print(f"{self.naam}, {self.geluid}, {self.huid}")

    def uitgebreide_info(self):
        print(f"{self.naam}, {self.geluid}, {self.huid}")
        print("Voedsel: ")
        print(", ".join(self.voedsel))
        print("===========")
        print("")


cat = Dier("zini", "kat")
cat.poten = 4
cat.voedsel = ["muizen", "paté", "vogels", "insecten"]
cat.geluid = "miauw"
cat.huid = "vlekkenpels"

hond = Dier("lotje", "hond")
hond.poten = 4
hond.voedsel = ["brokken", "vlees", "schoenen"]
hond.geluid = "woef"
hond.huid = "bruine pels"

cat.uitgebreide_info()
hond.uitgebreide_info()
