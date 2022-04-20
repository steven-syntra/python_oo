class Klanten:

    def __init__(self):
        self.collection = []
        self.index = 0

    # werkwijze Elke (list comprehension)
    def __iter__(self):
        return (kla for kla in self.collection)

    # werkwijze Steven

    # def __iter__(self):
    #     self.index = 0
    #     return self

    # def __next__(self):
    #     if self.index < len(self.collection):
    #         k = self.collection[self.index]
    #         self.index += 1
    #         return k
    #     else:
    #         raise StopIteration

    def add_klant(self, naam):
        k = Klant(naam)
        self.collection.append(k)


class Klant:

    def __init__(self, naam):
        self.name = naam
        self.saldo = 0


# create Klanten object (this is a collection of Klant objects)
mijnklanten = Klanten()

# add items to collection
mijnklanten.add_klant("Peeters")
mijnklanten.add_klant("Janssens")
mijnklanten.add_klant("Willems")

# loop over collection
for klant in mijnklanten:
    print(klant.name, klant.saldo)

print("EOF")
