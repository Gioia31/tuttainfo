'''
Crea la classe Triangolo, la classe derivata TriangoloIsoscele e, da quest'ultima, la classe derivata TriangoloEquilatero.
'''
class Triangolo():

    def __init__(self, lato1, lato2, lato3):
        self.lato1 = lato1
        self.lato2 = lato2 
        self.lato3 = lato3

    def info_scaleno(self):
        print("Il triangolo è scaleno ")
        print("Il perimetro del triangolo è ", self.lato1 + self.lato2 + self.lato3)


class TriangoloIsocele(Triangolo):

    def __init__(self, lato1, lato2, lato3):
        super().__init__(lato1, lato2, lato3)

    def info_isoscele(self):
        print("Il triangolo è isoscele")
        print("Il perimetro del triangolo è", self.lato1+ self.lato2 + self.lato3)


class TriangoloEquilatero(TriangoloIsocele):

    def __init__(self, lato1, lato2, lato3):
        super().__init__(lato1, lato2, lato3)

    def info_equilatero(self):
        print("Il triangolo è equilatero")
        print("Il perimetro del triangolo è", self.lato1 * 3)


def main():

    lato1 = int(input("Inserisci la misura del primo lato: "))
    lato2 = int(input("Inserisci la misura del secondo lato: "))
    lato3 = int(input("Inserisci la misura del terzo lato: "))

    if lato1 != lato2 and lato1 != lato3 and lato2 != lato3:
        triangolo1 = Triangolo(lato1, lato2, lato3)
        triangolo1.info_scaleno()
    elif lato1 == lato2 and lato1 == lato3 and lato2 == lato3:
        triangolo1 = TriangoloEquilatero(lato1, lato2, lato3)
        triangolo1.info_equilatero()
    else:
        triangolo1 = TriangoloIsocele(lato1, lato2, lato3)
        triangolo1.info_isoscele()
        
main()