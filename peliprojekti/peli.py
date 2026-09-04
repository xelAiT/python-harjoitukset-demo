
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

        print("\nValitse jokin alla olevista komennoista:\nHauska fakta\nKuka olen?\nLopeta")
        valinta = input("Anna komento: ")

        if valinta == "Hauska fakta":
            print("Olet elossa...")

        if valinta == "Kuka olen?":
            print(player_name)
        
        if valinta == "Lopeta":
            print("Peli sulkeutuu")
            peli_käynnissä = False
