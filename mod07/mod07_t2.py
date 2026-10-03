
import random

def roll_dice(tahkojen_lkm):
    return random.randint(1,tahkojen_lkm)

nopan_koko = int(input("Anna nopan koko: "))

heitot = 0

while heitot != nopan_koko:
    heitot = roll_dice(nopan_koko)
    print(heitot)
