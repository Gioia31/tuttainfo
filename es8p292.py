'''
Crea una classe Quadrato con l'attributo lato e i metodi del perimetro e dell'area
'''
class Quadrato:

    def __init__(self, lato):
        self.lato = lato 

    def area(self):
        return self.lato * self.lato

    def perimetro(self):
        return self.lato * 4

def main():
    l = float(input("Inserisci il lato del quadrato "))
    quadrato = Quadrato(l)
    print("L'area del quadrato di lato", l, " è uguale a ", quadrato.area())
    print("Il perimetro del quadrato di lato", l," è uguale a ", quadrato.perimetro())

main()