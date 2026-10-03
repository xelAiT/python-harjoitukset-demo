
reppu = []

def lisaa_esine():
    
    esine = input("Syötä reppuun lisättävä esine: ")
    if esine:
        reppu.append(esine)
        print(f"-{esine}- on lisätty reppuun!")
    else:
        print("Et syöttänyt mitään esinettä.")

def nayta_reppu():

    print("- Repussa olevat esineet -")
    if not reppu:
        print("Reppusi on tyhjä.")
    else:
        print(reppu)

def fakta():

    import random

    fakta = ["Olet elossa...", "Joku on ovellasi...", "Näen sinut...", "Miksi näytät tuolta?",
              "Lopeta tämän pelin pelaaminen.", "Sinun kannattaisi mennä ulos.", "Mitäpä tässä."]

    faktat = random.choice(fakta)
    print(faktat)


player_name = input("Anna nimesi: ")
player_age = input("Anna ikäsi: ")

print("Antamasi tiedot:")
print("Nimesi on:", player_name)
print("Ikäsi on:", player_age)

age = int (player_age)

if age < 12:
    print("Olet alaikäinen, ikäraja pelille on 12 vuotta. Peli sulkeutuu.")

else:
    print("\nTervetuloa peliin!")

    peli_käynnissä = True
    while peli_käynnissä:

        print("\n--- Päävalikko ---\n 1 - Lisää reppuun esine\n 2 - Tarkastele repun sisältöä\n 3 - Kerron sinulle jotain hauskaa!\n 4 - Lopeta peli")
        valinta = input("Valitse komento (1, 2, 3, 4): ")

        if valinta == "1":
            lisaa_esine()

        if valinta == "2":
            nayta_reppu()
        
        if valinta == "3":
            fakta()

        if valinta == "4":
            print("Peli sulkeutuu")
            peli_käynnissä = False
