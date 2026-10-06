
luvut = []

while True:
    luku = input("Anna luku: ")

    if luku == "":
        break
    luvut.append(luku)

if luvut:
    
    luvut.sort(reverse=True)

    viisi_suurinta = luvut[:5]

    print("Viisi suurinta suurimmasta alkaen:")

    for luku in viisi_suurinta:
        print(luku)