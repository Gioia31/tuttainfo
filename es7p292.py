'''
Elenca proprietà e metodi della classe motociclo
'''
class Motociclo:

    def __init__(self, ruote, marca, peso, velocità_max):
        self.ruote = ruote
        self.marca = marca
        self.peso = peso 
        self.velocità_max = velocità_max

    def info(self):
        print("Il motociclo di marca", self.marca, " ha ", self.ruote," ruote, pesa ", self.peso, "; la velocità massima raggiungibile è ", self.velocità_max)

def main():
    ruote = int(input("Inserisci il numero di ruote del motociclo "))
    marca = str(input("Inserisci la marca del motociclo "))
    peso = float(input("Inserisci il peso del motociclo "))
    velocità_max = int(input("Insersci la velocità massima raggiungibile dal motociclo "))
    motociclo1 = Motociclo(ruote, marca, peso, velocità_max)
    motociclo1.info()

main()