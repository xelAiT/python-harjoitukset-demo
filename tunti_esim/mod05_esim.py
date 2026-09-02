'''
suorita = True

while suorita:
    print("Tämä printtaantuu vain kerran")
    suorita = False

print("Suoritus loppui")

luku = 1    # alkuarvo / kierrosmuuttuja

while luku <= 5:    # ehto
    print(luku)
    #luku = luku + 1 # muuttajan arvon muuttaminen
    luku += 1

print("Jatketaan ohjelmaa")


#############################################


luku = int(input("Anna luku josta laskemme alsapäin: "))

while luku >= 1:
    print(luku)
    luku -= 1



##############################################



salasana = input("Anna salasana: ")

while salasana != "salasana":
    print("Väärä salasana")
    salasana = input("Anna salasana uudestaan: ")

'''

#######################################################3


# while / else rakenne
# suorite siirtyy else-haaraan kun toistoehto on epätosi   
# sitä ei voi suriteta jos poistutaan BREAK-lauseella
# else rakenne on harvemmin käytetty

'''
komento = input("Anna komento (lopeta, APUA): ").strip().lower()

while komento != "lopeta":
    if komento == "apua": # komento == "APUA" or komento == "apua":
        break
    print("Annoit komennon: ", komento)
    komento = input("Anna uusi komento: ")

else:
    print("Annoit käskyn lopeta!")

print("Ohjelma jatkuu")


######################################################


import random

noppa1 = noppa2 = heitot = 0

while (noppa1 != 6 or noppa2 != 6):

    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    print(noppa1, noppa2)
    heitot = heitot + 1

print(f"Tarvittiin {heitot:d} heittoa.")

'''
###############################################


eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1


    #############################################


import random
pelikerta = 0
heitot = 0
while pelikerta < 1000:

    noppa1 = noppa2 = 0
    while (noppa1 != 6 or noppa2 != 6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        print(noppa1, noppa2)
        heitot = heitot + 1
    pelikerta += 1

print("Pelikertoja meillä oli: " pelikerta)
print(f"Tarvittiin {heitot:d} heittoa.")