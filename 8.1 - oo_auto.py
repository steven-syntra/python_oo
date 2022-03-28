class Auto:

    """
    klasse Auto: verplichte attributen:
    merk (string), type (string), bouwjaar (int), brandstof (string)
    """

    def __init__(self, merk, type, jaar, stof):
        self.merk = merk
        self.type = type
        self.bouwjaar = jaar
        self.brandstof = stof

    def print_info(self):
        print(self.merk, self.type)
        print("Bouwjaar: %s" % self.bouwjaar)
        print("Brandstof: %s" % self.brandstof)
        print()


car1 = Auto("Volkswagen", "Kever", 1966, "Benzine")
car2 = Auto("Renault", "Twingo", 2008, "Diesel")
car3 = Auto("Fiat", "500", 2013, "LPG")
car3 = Auto()

wagenpark = [car1, car2, car3]

tel = 0
for wagen in wagenpark:
    tel += 1
    print("WAGEN", tel)
    wagen.print_info()
