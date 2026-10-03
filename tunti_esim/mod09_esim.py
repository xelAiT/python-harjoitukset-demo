
k2_rotu1 = "mopsi"
k1_nimi = "nipsu"
k1_synt = 2016

k2_rotu2 = "noutaja"
k2_nimi = "muikku"
k2_synt = 2008

k3_rotu3 = "pystkorva"
k3_nimi = "kimmo"
k3_synt = 2022

'''
class Koira:
    pass

# Luokka on kuin suunnitelma. Olio on sen perusteella rakennettu yksilö
koira1 = Koira()
koira2 = Koira()

koira1.nimi = "nipsu"
koira1.rotu = "mopsi"

koira2.nimi = "muikku"
koira2.rotu = "noutaja"

print("Ensimmäisen koiran nimi:", koira1.nimi)
print("Ensimmäisen koiran rotu:", koira1.rotu)

print("Toisen koiran nimi:", koira2.nimi)
print("Toisen koiran rotu:", koira2.rotu)
'''

# teimme juuri luokan Koira ilman ominaisuuksia
# tämän jälkeen määärittelemme ominaisuudet yksi kerrallaan == 
# työlästä!!

# näin teemme oikeasti:

class Koira:
    # Luokkamuuttaja
    tehty = 0

    koiran_lelut = ["Purulelu"]

    def __init__(self, nimi, rotu, syntymävuosi, haukahdus="Viuviu"):
        self.nimi = nimi
        self.rotu = rotu
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        self.luokitus = "nisäkäs"
        Koira.tehty += 1

    def hauku(self, kerrat):
        print(f"{self.nimi} tervehtii sinua")
        for i in range(kerrat):
            print(self.haukahdus)

koira1 = Koira("Nipsu", "Mopsi", 2016, "Wof Wof")
koira2 = Koira("Muikku", "Noutaja", 2008, "Hau Hau")
koira3 = Koira("Kimmo", "Pystykora", 2022, "Huutista")

koira1.hauku(2)
print()
koira2.hauku(3)
print()
koira3.hauku(1)

print(f"\nEnsimmäisen koiran nimi on {koira1.nimi} ja rotu {koira1.rotu}, vuosi {koira1.syntymävuosi}")
print(f"Toisen koiran nimi on {koira2.nimi} ja rotu {koira2.rotu}, vuosi {koira2.syntymävuosi}")

print()
print("---------------------------------------------------")

class Player:
    def __init__(self, name, skill_level, inventory):
        self.name = name
        self.skill_level = skill_level
        self.inventory = inventory

    def show_info(self):
        pass

player1 = Player("Player 1", 10, {"map", "knife"})
player2 = Player("Player 2", 20, {"axe"})

inventaario = {"hakku", "kokis", "vasara"}
inventaario2 = ["hakku", "kokis", "vasara"]

print(f"Pelaajan 1 nimi on {player1.name} ja taso on {player1.skill_level}")