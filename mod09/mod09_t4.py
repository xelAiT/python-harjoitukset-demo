import random

class Auto:

    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
             self.nopeus = self.huippunopeus

        elif self.nopeus < 0:
             self.nopeus = 0

    def kulje(self, tunnit):
         self.kuljettu_matka += self.nopeus * tunnit


autot = []

for i in range(1, 11):
     rekkari = f"ABC-{i}"
     huippunopeus = random.randint(100, 200)
     autot.append(Auto(rekkari, huippunopeus))

kilpailu_jatkuu = True

while kilpailu_jatkuu:
     for auto in autot:
          muutos = random.randint(-10, 15)
          auto.kiihdytä(muutos)

          auto.kulje(1)

          if auto.kuljettu_matka >= 1000:
               kilpailu_jatkuu = False

print(f"{'Rekisteri':<10} | {'Huippunopeus':<10} | {'Nopeus nyt':<11} | {'Kuljettu matka'}")
print('-------------------------------------------------------------')
for auto in autot:
    print(f"{auto.rekkari:<10} | {auto.huippunopeus:>3} km/h     | {auto.nopeus:>3} km/h    | {auto.kuljettu_matka:>7.1f} km")