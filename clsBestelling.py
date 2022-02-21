class Bestelling:

    def __init__(self, naam, datum):
        self.name = naam
        self.date = datum
        self.dict = {}

    def AddProduct(self, product, aantal):
        self.dict[product] = aantal

    def PrintOut(self):
        som = 0
        print("Bestelling van ", self.name, " op ", self.date, ":")

        for product, aantal in self.dict.items():
            print("%s , prijs: %s, aantal: %s" % (product.naam, product.prijs, aantal))
            som += product.prijs * aantal

        print("Totaal: %s" % som)
