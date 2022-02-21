import random

soorten = ("Harten", "Schoppen", "Klaveren", "Ruiten")
rangen = ("Aas", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Boer", "Dame", "Heer")


class Kaart:
    soort = 0
    rang = 0

    def __init__(self, soort=0, rang=0):
        if soort in range(len(soorten)):
            self.soort = soorten[soort]
        else:
            print("Onbekende soort")

        if rang in range(len(rangen)):
            self.rang = rangen[rang]
        else:
            print("Onbekende rang")

    def print_kaart(self):
        print(self.soort, self.rang)


class Spel:
    kaarten = []
    index = 0

    def __init__(self):
        for s in range(len(soorten)):
            for r in range(len(rangen)):
                k = Kaart(s, r)
                self.kaarten.append(k)

    def print_all(self):
        for i, p in enumerate(self.kaarten):
            print(str(i + 1) + " ", end="")
            p.print_kaart()

    def get_random_kaart(self):
        self.index = random.randint(0, 51)
        print(self.index)
        self.kaarten[self.index].print_kaart()


spel = Spel()
print("Alle kaarten in het spel:")
spel.print_all()
print("")
print("Een willekeurig geselecteerde kaart:")
spel.get_random_kaart()
