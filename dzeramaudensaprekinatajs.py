def aprekins(sk1, sk2):
    atlikums = sk2 - sk1 
    if atlikums >0:
        print("Tev vēl jāizdzer", atlikums, "mililitri.")
    else:
        print("Tu esi pārsniedzis dienas mērķi par", -atlikums, "mililitriem.")

def ieteicamais(dzimums):
    if dzimums == "vīrietis":
        print("Tavs mērķis ir 3700 mililitri.")
        return 3700
    elif dzimums == "sieviete":
        print("Tavs mērķis ir 2700 mililitri")
        return 2700
    else:
        print("Nepareiza ievade.")
        return 0


ievade = input("Vai tu esi vīrietis vai sieviete?")
lielaks = ieteicamais(ievade)

if lielaks ==0: 
    print("Nepareiza ievade.")
else:
    kopaizdzerts = 0
    
while True:
    dzeramais = int(input("Ievadi cik mililitrus ūdens esi izdzēris/usi:"))
    kopaizdzerts += dzeramais 

    aprekins(kopaizdzerts, lielaks)

    turpinat = input("Vai gribi turpināt? (y vai n):")
    if turpinat !="y":
        break
