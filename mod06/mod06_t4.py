
kaupungit = []

for i in range(5):
    kaupunki = input(f"Syötä kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("Syöttämäsi kaupungit järjestyksessä:")

for kaupunki in kaupungit:
    print(kaupunki)
