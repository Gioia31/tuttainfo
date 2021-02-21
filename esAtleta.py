class Atleta:
    def __init__ (self, name, age, surname, weight, height):
        self.name = name
        self.age = age
        self.surname = surname
        self.weight = weight
        self.height = height
        self.visitaMedica = False

    def effettua_visita(self):
        self.visitaMedica = True

    def info(self):
        print("L'atleta si chiama: ", self.name, self.surname)
        print("Età: ", self.age)
        print("Peso: ", self.weight, " kg")
        print("Altezza: ", self.height, " cm")
        
    
    def squadra( self, team):
        self.team = team
        print("L'atleta ", self.name, self.surname, " gioca nella squadra ", self.team)

def main():
    name = input("Inserisci il nome dell'atleta ")
    age = input("Inserisci l'età dell'atleta ")
    surname = input("Inserisci il cognome dell'atleta ")
    weight = int(input("Inserisci il peso dell'atleta "))
    height = int(input("Inserisci l'altezza dell'atleta "))
    team = input("Inserisci la squadra in cui gioca l'atleta ")
    atleta = Atleta(name, surname, age, weight, height)
    visita = str(input("L'atleta si è sottoposto alla visita medica? "))
    if visita.upper == "SI":
        atleta.effettua_visita()
    atleta.info()
    atleta.squadra(team)

main()





    

        