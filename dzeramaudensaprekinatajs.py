def aprekins(sk1, sk2): #galvenais aprēķins
    atlikums = sk2 - sk1 
    if atlikums >0: #cik vēl jāizdzer
        print("Tev vēl jāizdzer", atlikums, "mililitri.")
    else: #par cik pārsniedz mērķi
        print("Tu esi pārsniedzis dienas mērķi par", -atlikums, "mililitriem.")

def ieteicamais(dzimums): #cik katram dzimumam ir jāizder ūdens dienā
    if dzimums == "vīrietis":
        print("Tavs mērķis ir 3700 mililitri.")
        return 3700
    elif dzimums == "sieviete":
        print("Tavs mērķis ir 2700 mililitri")
        return 2700
    else: #ja ievada kautko citu kas nav vīrietis vai sieviete tad parādās kļūda
        print("Nepareiza ievade.")
        return 0


ievade = input("Vai tu esi vīrietis vai sieviete?") #datu ievade
lielaks = ieteicamais(ievade)

if lielaks ==0: 
    print("Nepareiza ievade.")
else:
    kopaizdzerts = 0
    
while True: #ievade izdzertajam udens daudzumam un cikls
    dzeramais = int(input("Ievadi cik mililitrus ūdens esi izdzēris/usi:"))
    kopaizdzerts += dzeramais 

    aprekins(kopaizdzerts, lielaks)

    turpinat = input("Vai gribi turpināt? (y vai n):") #turpinat ievadit vai parstat ciklu
    if turpinat !="y":
        break
