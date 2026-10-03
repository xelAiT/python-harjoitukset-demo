
import random

def roll_dice():
    return random.randint(1,6)

heitot = 0

while heitot != 6:
    print(roll_dice())
