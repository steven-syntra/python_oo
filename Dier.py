class Dier:
    naam = ""
    poten = 0
    voedsel = []
    geluid = ""
    huid = ""


cat = Dier()
cat.naam = "zini"
cat.poten = 4
cat.voedsel = [ "muizen", "paté", "vogels", "insecten" ]
cat.geluid = "miauw"
cat.huid = "vlekkenpels"

hond = Dier()
hond.naam = "lotje"
hond.poten = 4
hond.voedsel = [ "brokken" ,"vlees", "schoenen" ]
hond.geluid = "woef"
hond.huid = "bruine pels"

print( f"{cat.naam}, {cat.geluid}, {cat.huid}")
print( f"{hond.naam}, {hond.geluid}, {hond.huid}")





