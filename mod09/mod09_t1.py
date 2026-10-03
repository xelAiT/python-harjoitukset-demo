
class Auto:

    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus: {auto1.rekkari}\nHuippunopeus: {auto1.huippunopeus}\nNopeus:{auto1.nopeus}\nKuljettu matka: {auto1.kuljettu_matka}")