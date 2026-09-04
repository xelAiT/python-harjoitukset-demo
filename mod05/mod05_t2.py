
muunnos = 2.54

while True:

    tuuma = float(input("Anna tuumien määrä: "))

    if tuuma <= 0:
        break

    cm = tuuma * muunnos
    print(f"{tuuma} tuumaa on {cm} cm ")
