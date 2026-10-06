
import random

class Esine:
    def __init__(self, nimi):
        self.nimi = nimi



class Pelaaja:
    def __init__(self, aloitus_huone, nimi):
        self.nimi = nimi
        self.nykyinen_huone = aloitus_huone
        self.reppu = []

    def poimi_esine(self, esine):
        self.reppu.append(esine)

    def onko_esine_repussa(self, esineen_nimi):
        for esine in self.reppu:
            if esine.nimi.lower() == esineen_nimi.lower():
                return True
        return False



 
class Huone:
    def __init__(self, nimi, kuvaus):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.huoneet = []
        self.esineet = []

    def lisaa_huone(self, toinen_huone):
        if toinen_huone not in self.huoneet:
            self.huoneet.append(toinen_huone)

    def lisaa_esine(self, esine):
        self.esineet.append(esine)




class Morko:
    def __init__(self, aloitus_huone):
        self.nykyinen_huone = aloitus_huone

    def liiku_satunnaisesti(self, kaikki_huoneet):
        self.nykyinen_huone = random.choice(kaikki_huoneet)
