
'''
player_name = input("Anna nimesi: ")
player_age = input("Anna ikäsi; ")

print("Antamasi tiedot:")
print("Nimesi on:", player_name)
print("Ikäsi on:", player_age)
'''

peli_käynnissä = True
# main loop
print("Tervetuloa peliin!")

while peli_käynnissä:
    print("Valitse minne mennään (j tai l)")
    # j jatkaa peliä ja l lopettaa
    valinta = input("Anna komento: ")

    if valinta == "j":
        print("Jatkoit peliä")
        
    if valinta == "l":
        peli_käynnissä = False

    else:
        print("Koitappa uuestaan...")