
import random

kuutio = int(input("Anna heitettävien arpakuutioden määrä: "))

heitot = 0

for i in range(kuutio):
    arpa = random.randint(1,6)
    heitot = heitot + arpa
    print(arpa)

print(f"Silmälukujen summa on: {heitot}")