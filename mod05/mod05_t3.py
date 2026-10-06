
syote = input("Anna luku: ")

if syote != "":
    
    pienin = float(syote)
    suurin = float(syote)

    while True:
        syote = input("Anna luku: ")
        if syote == "":
            break

        luku = float(syote)
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

    print("Pienin antamasi luku:", pienin)
    print("Suurin antamasi luku:", suurin)

else:
    print("Et antanut yhtään lukua.")
