'''
Data la classe Motociclo creata nel problema 7, deriva la classe Ciclomotore.
Aggiungi le proprietà opportune e modifica il metodo che consente di visualizzare
i valori delle proprietà.
'''

class Motociclo:

    def __init__(self, ruote, marca, peso, velocità_max):
        self.ruote = ruote
        self.marca = marca
        self.peso = peso 
        self.velocità_max = velocità_max

    def info(self):
        print("Marca: ", self.marca)
        print("Numero ruote:  ", self.ruote)
        print("Peso: ", self.peso, " kg")
        print("Velocità massima raggiungibile: ", self.velocità_max, " Km/h")

class Ciclomotore(Motociclo):

    def __init__(self, ruote, marca, peso, velocità_max, cilindrata):
        super().__init__(ruote, marca, peso, velocità_max)
        self.cilindrata = cilindrata

    def info_ciclomotore(self):
        print("Marca: ", self.marca)
        print("Numero ruote:  ", self.ruote)
        print("Peso: ", self.peso, " kg")
        print("Velocità massima raggiungibile: ", self.velocità_max, " Km/h")
        print("Cilindrata: ", self.cilindrata)

def main():
    ruote = int(input("Inserisci il numero di ruote " ))
    marca = str(input("Inserisci la marca "))
    peso = float(input("Inserisci il peso "))
    velocità_max = int(input("Insersci la velocità massima raggiungibile "))
    motociclo1 = Motociclo(ruote, marca, peso, velocità_max)
    motociclo1.info()
    cilindrata = int(input("Inserisci la cilindrata "))
    ciclomotore = Ciclomotore(ruote, marca, peso, velocità_max, cilindrata)
    ciclomotore.info_ciclomotore()

main()