
vuodenajat = ("kevät", "kesä", "syksy", "talvi")
jarjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))
viikonpaiva = viikonpaivat[jarjestysnumero - 1]
print(f"{jarjestysnumero}. viikonpäivä on {viikonpaiva}.")