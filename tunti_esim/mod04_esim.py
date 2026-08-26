
# Kolikonheitto sim.

import random

random_number = random.randint(0,1)
print(random_number)

if random_number == 0:
    result = 'kruuna'

if random_number == 1:
    result = 'klaava'

print(f'Heitit kolikkoa ja sait: {result}n.')


suutari = input("Anna suutarin nimi: ")
räätäli = input("Anna räätälin nimi: ")

if suutari==räätäli:
    print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")