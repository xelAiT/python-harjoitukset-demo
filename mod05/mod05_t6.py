


import random

N = 100     # kaikkien pisteiden lukumäärä
counter = 0     # lasketaan ympyrään osuneiden pisteiden lukumäärä

while counter < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    print(f("Arvotun pisteen koordinaatit, x: {x}, y: {y}"))
    counter += 1

    if x ** 2 + y ** 2 < 1:
        n = n + 1
        print("Piste on ympyrän sisällä.")

print(f("Pisteitä arvottu yhteensä {N}, joista ympyrän sisälle osui {n} kpl."))

# TODO: Laskee pii annetulla kaavalla ja tulosta. Kokeile myös eri N arvoilla