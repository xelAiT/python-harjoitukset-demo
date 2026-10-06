
def parilliset_lista(lista):

    parilliset = []

    for luku in lista:

        if luku % 2 == 0:

            parilliset.append(luku)

    return parilliset

alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suodatettu_lista = parilliset_lista(alkuperainen_lista)

print(f"Alkuperäinen lista: {alkuperainen_lista}")
print(f"Parilliset lista: {suodatettu_lista}")