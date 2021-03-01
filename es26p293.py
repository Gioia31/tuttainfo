'''
Deriva dalla classe Quadrato una nuova classe Rettangolo aggiungendo un secondo lato per l'altezza e 
riscrivi i metodi per il calcolo del perimetro e dell'area.
'''

class Quadrato:

    def __init__(self, lato):
        self.lato = lato 
    def area(self):
        return self.lato * self.lato
    def perimetro(self):
        return self.lato * 4

class Rettangolo(Quadrato):

    def __init__(self, lato, altezza):
        super().__init__(lato)
        self.altezza = altezza
    def perimetro_rettangolo(self):
        return (self.lato * self.altezza)/2
    def area_rettangolo(self):
        return self.lato * self.altezza

def main():

    l = float(input("Inserisci il lato del quadrato e del rettangolo "))
    quadrato = Quadrato(l)
    print("L'area del quadrato di lato", l, " è uguale a ", quadrato.area())
    print("Il perimetro del quadrato di lato", l," è uguale a ", quadrato.perimetro())

    altezza = int(input("Inserisci l'altezza del rettangolo "))
    rettangolo = Rettangolo(l, altezza)
    print("Il perimetro del rettangolo è ", rettangolo.perimetro_rettangolo())
    print("L'area del rettangolo è ", rettangolo.area_rettangolo())

main()