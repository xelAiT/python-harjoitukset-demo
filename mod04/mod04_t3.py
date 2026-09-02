

sukupuoli = input("Kerro biologinen sukupuolesi: ")
gl = float (input("Kerro hemoglobiini arvosi: "))

if sukupuoli == "mies":
    if gl <= 133:
        print("Hemoglobiini arvosi on alhainen.")

    elif gl >= 196:
        print("Hemoglobiini arvosi on korkea.")

    else:
        print("Hemoglobiini arvosi on normaali")

if sukupuoli == "nainen":
    if gl <= 116:
        print("Hemoglobiini arvosi on alhainen.")

    elif gl >= 176:
        print("Hemoglobiini arvosi on korkea.")

    else:
        print("Hemoglobiini arvosi on normaali")