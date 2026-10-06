
from peli_paketti.peli_ydin import Peli
from peli_paketti.toiminnot import (tarkista_ika_ja_nimi, intro, nayta_tilanne, tarkista_esineet, kasittele_liikkuminen)
import sys

if __name__ == "__main__":
    pelaajan_nimi = tarkista_ika_ja_nimi()

    if pelaajan_nimi is not None:
        peli = Peli(pelaajan_nimi)
        intro(peli.pelaaja.nimi)

        while peli.kaynnissa:

            nayta_tilanne(peli.paiva, peli.max_paivat, peli.pelaaja.nykyinen_huone, peli.pelaaja.reppu)
            tarkista_esineet(peli)

            if peli.pelaaja.nykyinen_huone.nimi == "Pääovi":
                print("\nOlet pääovella. Ovi on lukittu ja sen edessä on paksuja lautoja.")
                if peli.pelaaja.onko_esine_repussa("Vasara") and peli.pelaaja.onko_esine_repussa("Koodi") and peli.pelaaja.onko_esine_repussa("Pääavain"):
                    print(f"\nHakkaat laudat rikki vasaralla, näppäilet löytämäsi koodin paneeliin ja avaat lukon avaimella!")
                    print(f"Pakenet talosta aurinkoiseen vapauteen!")
                    peli.kaynnissa = False
                    continue
                else:
                    print("Tarvitset Vasaran, Koodin ja Pääavaimen päästäksesi ulos.")

            seuraava_huone = kasittele_liikkuminen(peli.pelaaja.nykyinen_huone)

            if seuraava_huone == "LOPETA":
                print("Lopetit pelin. Mörkö sai sinut kiinni!")
                peli.kaynnissa = False
                continue
            elif seuraava_huone is None:
                continue

            peli.pelaaja.nykyinen_huone = seuraava_huone
            print("Liikut huoneeseen:", seuraava_huone.nimi)

            peli.morko.liiku_satunnaisesti(peli.kaikki_huoneet)

            if peli.pelaaja.nykyinen_huone == peli.morko.nykyinen_huone:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("MÖRKÖ PELÄSTYTTI SINUT!")
                print("Mörkö jäädyttää sinut!")
                print("Menetät tajuntasi...")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

                peli.paiva += 1
                peli.pelaaja.nykyinen_huone = peli.makuuhuone  # Palautetaan aloitus-makuuhuoneeseen

                if peli.paiva > peli.max_paivat:
                    print("\n==================================================")
                    print("GAME OVER")
                    print("==================================================")
                    print(f"5 päivää kului. Jäädyit osaksi sisustusta. Hävisit pelin, {peli.pelaaja.nimi}.")
                    peli.kaynnissa = False

                else:
                    input("\nPaina Enter herätäksesi uuteen päivään...")
