
class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)

class Hoitola:
    def __init__(self):
        # Syntyy assosiaatio
        self.koirat = []

    def koira_sisään(self, koira):
        self.koirat.append(koira)
        # pääsee nyt koiran (olion) ominaisuuksiin
        print(koira.nimi + " kirjattu sisään")
        # hoitola pääsee myös kutsumaan koiran metodeja
        # tämäkin on assosiaatio eli hoitola "tuntee" toisen olion

        print(koira.hauku(2))


# Pääohjelma

koira1 = Koira("Jaska", 2009)
koira2 = Koira("Kalle", 2014, "Huutista Huutista")

hoitola = Hoitola()
hoitola.koira_sisään(koira1)
hoitola.koira_sisään(koira2)