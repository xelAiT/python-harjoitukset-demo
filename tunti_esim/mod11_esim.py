
class Elain:

    def __init__(self, nimi, paino, synt_aika):
        self.nimi = nimi
        self.paino = paino
        self.synt_aika = synt_aika
        Elain.elainten_lkm += 1

    def liiku(self):
        print(f"{self.nimi} liikkuu jotenkin johonkin...")

    def kaikki_tiedot(self):
        print(f"Nimi: {self.nimi}, Paino: {self.paino/1000}, Syntymävuosi: {self.synt_aika}")


class Peto:
    def __init__(self, on_metsastaja):
        self.on_metsastaja = on_metsastaja


# Tässä esimerkissä ilves ei ole peto
class Ilves(Elain):

    def kilju(self):
        print(f"Ilves nimeltä {self.nimi} kiljuu!")

    def kaikki_tiedot(self):
        print(f"\nIlves")
        super().kaikki_tiedot()


# Karhu perii kaksi luokkaa
class Karhu(Elain, Peto):

    def __init__(self, nimi, paino, synt_aika, on_horroksessa, on_metsastaja):
        self.on_horroksessa = on_horroksessa
        # koska konstruktori ylikirjoitetaan, tarvitsee yliluokan konstruktoria kutsua
        # erikseen, jos sitä hakutaan hyödyntää
        super().__init__(nimi, paino, synt_aika)

        Elain.__init__(self, nimi, paino, synt_aika)

        Peto.__init__(self, on_metsastaja)

    def karju(self):
        print(f"Karhu nimeltä {self.nimi} karjuu!")

    def liiku(self):
        print(f"Karhu {self.nimi} möyrii eteenpäin.")

    def kaikki_tiedot(self):
        print(f"\nKarhu on metsästäjä: {self.on_metsastaja}, joka on nyt talviunilla: {self.on_horroksessa}")


class Elaintarha:

    def __init__(self, nimi="nimetön"):
        self.nimi = nimi
        self.elaimet = []

    def lisaa_elain(self, elain):
        self.elaimet.append(elain)

    def listaa_kaikki(self):
        print(f"Eläintarhan {self.nimi} kaikki eläimet ({len(self.elaimet)} kpl) ")
        print("=====================================")
        for elain in self.elaimet:
            elain.kaikki_tiedot()
            print("---")



uusi_elain = Elain("Joku elukka", 1500, 2025)
uusi_elain.liiku()

ilves1 = Ilves("Ilveskissa", 6500, 2025)
ilves1.liiku()
ilves1.kilju()

karhu1 = Karhu("Nalle", 155000, 2020, False, True)
karhu1.karju()
karhu1.liiku()

tarha = Elaintarha()
tarha.lisaa_elain(ilves1)
tarha.lisaa_elain(karhu1)
tarha.lisaa_elain(Karhu(f"Eläimiä luotu yhteensä: {Elain.elainten_lkm}"))