
import random

def roll_dice():
    return random.randint(1,6)

while True:

    arpa = roll_dice()
    print(arpa)

    if arpa == 6:
        break

