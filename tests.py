# ievade = int(input("ievadiet skaitli :"))

# print(ievade)
# lielaks = ievade + 1
# print("skaitlis kas par 1 lielas :", lielaks)\

# print(6==1)

# skaitlis = int(input("Iedod skaitli: "))

# if (skaitlis>=20):
#     print("liels")
# elif(skaitlis<5):
#     print("mazs")
# elif(skaitlis>10 and skaitlis<20):
#     print("videjs")
# else:
#     print("normal")

# num1 = int(input("pirmais skaitlis: "))
# num2 = int(input("otrais skaitlis: "))

# print(aprekins(num1,num2))


def aprekins(num1, num2):
    reiz = num1*num2
    if (reiz<=20):
        return reiz
    return num1+num2

for i in range(-2,10,3): #range (sakums, beigas(neieskaitot), solis)
    print(aprekins(3,i))

answ = "y"
while(answ == "y"):
    sk1 = int(input("pirmais: "))
    sk2  = int(input("otrais: "))
    print (aprekins(sk1,sk2))
    answ = input("turpinat? ('y' 'n'): ")
