
import random

from peli_paketti.luokat import Huone, Esine, Pelaaja, Morko

class Peli:
    def __init__(self, pelaajan_nimi):

        self.makuuhuone = Huone("Makuuhuone", "Pimeä huone, jossa on vanha narskuva sänky.")
        self.kaytava = Huone("Käytävä", "Pitkä ja karmiva käytävä. Seinillä on vanhoja tauluja.")
        self.keittiö = Huone("Keittiö", "Haisee pilaantuneelle ruoalle.")
        self.olohuone = Huone("Olohuone", "Suuri huone, jossa on pölyisiä huonekaluja.")   
        self.paaovi = Huone("Pääovi", "Suuri lukittu ovi jonka edessä on lautoja ja jonkin sortin paneeli johon voi syöttää koodin.")                            # huone oliot
        self.vessa = Huone("Vessa", "Pieni vessa, jossa on likainen lavuaari ja rikkinäinen peili.")
        self.sauna = Huone("Sauna", "Sauna on yllättävän siisti ja lämmin. Mörkö vaikuttaa olevan saunamiehiä.")
        self.komero = Huone("Komero", "Pieni mutta yllättävän kotoisa. Mitä se nyt meinaakaan?")
        self.ullakko = Huone("Ullakko", "Et näe kauemmas kuin vain sormenpäihin asti. Täällä on jokun aikaisemma asukkaan luuranko.")

        self.kaikki_huoneet = [self.makuuhuone, self.kaytava, self.keittiö, self.olohuone, self.paaovi, self.vessa, self.sauna, self.komero, self.ullakko]



        self.makuuhuone.lisaa_huone(self.komero)
        self.komero.lisaa_huone(self.makuuhuone)

        self.makuuhuone.lisaa_huone(self.kaytava)
        self.kaytava.lisaa_huone(self.makuuhuone)

        self.kaytava.lisaa_huone(self.ullakko)
        self.ullakko.lisaa_huone(self.kaytava)

        self.kaytava.lisaa_huone(self.keittiö)
        self.keittiö.lisaa_huone(self.kaytava)
                                                             # huoneiden väliset kulkuyhteydet
        self.kaytava.lisaa_huone(self.olohuone)
        self.olohuone.lisaa_huone(self.kaytava)

        self.olohuone.lisaa_huone(self.keittiö)
        self.keittiö.lisaa_huone(self.olohuone)

        self.kaytava.lisaa_huone(self.paaovi)
        self.paaovi.lisaa_huone(self.kaytava)

        self.kaytava.lisaa_huone(self.vessa)
        self.vessa.lisaa_huone(self.kaytava)

        self.vessa.lisaa_huone(self.sauna)
        self.sauna.lisaa_huone(self.vessa)



        self.vasara = Esine("Vasara")
        self.koodi = Esine("Koodi")
        self.avain = Esine("Pääavain")

        mahdolliset_huoneet = [self.kaytava, self.keittiö, self.olohuone, self.vessa, self.sauna, self.komero, self.ullakko]            # esineet ja niiden piilopaikat
        

        self.vasara_huone_olio = random.choice(mahdolliset_huoneet)
        self.koodi_huone_olio = random.choice(mahdolliset_huoneet)
        self.avain_huone_olio = random.choice(mahdolliset_huoneet)
        
        self.vasara_huone_olio.lisaa_esine(self.vasara)
        self.koodi_huone_olio.lisaa_esine(self.koodi)
        self.avain_huone_olio.lisaa_esine(self.avain)


        self.pelaaja = Pelaaja(self.makuuhuone, pelaajan_nimi)
        self.morko = Morko(self.keittiö)
        
        self.paiva = 1
        self.max_paivat = 5
        self.kaynnissa = True
