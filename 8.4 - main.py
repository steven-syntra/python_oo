from clsProduct import Product
from clsBestelling import Bestelling

# 4 verschillende producten definiëren
p1=Product("iPhone 7", 300)
p2=Product("Samsung Galaxy P6", 250)
p3=Product("Huawei XL", 270)
p4=Product("LG 7800", 214)

# een bestelling maken voor een klant
b=Bestelling("Piet Peeters", "01/11/2018")
b.AddProduct(p1, 2)   # 2 iPhones toevoegen
b.AddProduct(p2, 3)   # 3 Samsungs toevoegen
b.PrintOut()            # samenvatting van de bestelling weergeven
