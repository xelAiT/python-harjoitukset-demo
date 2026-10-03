
class Hissi:

    def __init__(self, alin_kerros, ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def siirry_kerrokseen(self, kohdekerros):
            print(f"Siirrytään kerrokseen: {kohdekerros}")
            while self.nykyinen_kerros < kohdekerros:
                self.kerros_ylös()
            while self.nykyinen_kerros > kohdekerros:
                self.kerros_alas()
        

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa: {self.nykyinen_kerros}")


    def kerros_alas(self):
        if self.nykyinen_kerros < self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa: {self.nykyinen_kerros}")


hissi1 = Hissi(1, 12)
hissi2 = Hissi(5, 20)

#print(hissi1.nykyinen_kerros)
#print(hissi2.nykyinen_kerros)


hissi1.siirry_kerrokseen(6)