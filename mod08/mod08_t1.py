
vuodenajat = ("talvi", "talvi", "kevät","kevät","kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

jarjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))

kuukausi = vuodenajat[jarjestysnumero - 1]

print(f"{jarjestysnumero}. kuukausi on {kuukausi}.")
