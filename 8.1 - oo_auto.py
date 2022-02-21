class Auto:

    merk = ""
    type = ""
    bouwjaar = 0
    brandstof = ""

    def __init__(self, merk, type, jaar, stof):
        self.merk = merk
        self.type = type
        self.bouwjaar = jaar
        self.brandstof = stof

    def Info(self):
        print( self.merk, self.type )
        print( "Bouwjaar: %s" % self.bouwjaar )
        print( "Brandstof: %s" % self.brandstof )
        print()

car1 = Auto("Volkswagen", "Kever", 1966, "Benzine")
car2 = Auto("Renault", "Twingo", 2008, "Diesel")
car3 = Auto("Fiat", "500", 2013, "LPG")

wagenpark = [ car1, car2, car3 ]

tel=0
for wagen in wagenpark:
    tel += 1
    print("WAGEN", tel)
    wagen.Info()
