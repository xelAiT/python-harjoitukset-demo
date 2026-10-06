import os

def tarkista_ika_ja_nimi():
    print("--- IKÄTARKISTUS ---")
    player_name = input("Anna nimesi: ")
    player_age = input("Anna ikäsi: ")
    
    if int(player_age) < 12:
        print("Olet alaikäinen, ikäraja pelille on 12 vuotta.")
        print("Ohjelma sammuu.")
        return None


    else:
        print(f"\nTervetuloa peliin, {player_name}!")
        return player_name



######################################################################################################################################



def intro(pelaajan_nimi):
    nykyinen_hakemisto = os.path.dirname(os.path.abspath(__file__))
    juuri_hakemisto = os.path.dirname(nykyinen_hakemisto)
    
    intro_polku = os.path.join(juuri_hakemisto, "intro.txt")
    ohjeet_polku = os.path.join(juuri_hakemisto, "ohjeet.txt")

    try:
        with open(intro_polku, "r", encoding="utf-8") as tiedosto_intro:
            sisalto_intro = tiedosto_intro.read().strip()
            print(sisalto_intro, end="")
            
        print(f", {pelaajan_nimi}.\n")
    
        with open(ohjeet_polku, "r", encoding="utf-8") as tiedosto_ohjeet:
            sisalto_ohjeet = tiedosto_ohjeet.read()
            print(sisalto_ohjeet)
            
    except FileNotFoundError:
        print(f"\nTekstitiedostoja ei löytynyt: {juuri_hakemisto}")
        print(f"Aloitetaan peli ilman niitä. Tervetuloa peliin, {pelaajan_nimi}!")

    input("\nPaina Enter jatkaaksesi...")


######################################################################################################################################


def nayta_tilanne(paiva, max_paivat, huone, reppu):

    print("\n----------------------------------------")
    print("PÄIVÄ", paiva, "/", max_paivat)
    print(f"Olet huoneessa: {huone.nimi}")
    print(huone.kuvaus)
    
    if len(reppu) == 0:
        print("Repussasi on: Tyhjä")

    else:
        nimilista = [esine.nimi for esine in reppu]
        print("Repussasi on:", ", ".join(nimilista))
    print("----------------------------------------")


######################################################################################################################################


def tarkista_esineet(peli_olio):

    huone = peli_olio.pelaaja.nykyinen_huone
    for esine in list(huone.esineet):
        print(f"Näet lattialla esineen: {esine.nimi}")
        valinta = input(f"Haluatko ottaa esineen {esine.nimi}? (kyllä/ei): ").strip().lower()
        
        if valinta in ["kyllä", "k"]:
            peli_olio.pelaaja.poimi_esine(esine)
            huone.esineet.remove(esine)
            print(f"Poimit esineen: {esine.nimi}")



######################################################################################################################################



def kasittele_liikkuminen(nykyinen_huone):
    print("Voit mennä seuraaviin huoneisiin: ", end="")
    naapurien_nimet = [huone.nimi for huone in nykyinen_huone.huoneet]
    print(", ".join(naapurien_nimet))

    syote = input("Mihin huoneeseen menet? (tai kirjoita 'lopeta'): ").strip()
    
    if syote.lower() == "lopeta":
        return "LOPETA"
        
    for huone in nykyinen_huone.huoneet:
        if huone.nimi.lower() == syote.lower():
            return huone
            
    print("Et voi mennä sinne suoraan tästä huoneesta. Kirjoita huoneen nimi tarkasti.")
    return None
