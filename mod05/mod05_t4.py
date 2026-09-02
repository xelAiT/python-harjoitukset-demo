
import random

oikea_num = random.randint(1,10)
arvaus = int(input("Arvaa numero 1 ja 10 välillä: "))

while arvaus != oikea_num:

    if arvaus <= oikea_num:
        print("Liian pieni arvaus.")
        arvaus = int(input("Kokeile uudestaan: "))

    if arvaus >= oikea_num:
        print("Liian suuri vastaus.")
        arvaus = int(input("Kokeile uudestaan: "))

    else:
        print("Arvasit oikein!")