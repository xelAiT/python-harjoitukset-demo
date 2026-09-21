
class Auto:

    def __init__(self, rekkari, huippunopeus):
        self.rekisteritunnus = rekkari
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
         self.kuljettu_matka += self.nopeus + tunnit

def moikka():
        print("brum brum")

auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus: {auto1.rekisteritunnus}")
print(f"Huippunopeus: {auto1.huippunopeus}")
print(f"Nopeus: {auto1.nopeus}")
print(f"Kuljettu matka: {auto1.kuljettu_matka}")

moikka()
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print("Auton nopeus kiihdytyksen jälkeen: ",auto1.nopeus)

auto1.kulje(1.5)
print("Kuljettu matka 1.5h jälkeen: ", auto1.kuljettu_matka)

auto1.kiihdytä(-200)
print("Auton nopeus jarrutuksen jälkeen: ",auto1.nopeus)
