class Atleta():

    def __init__(self, name, surname, age, weight, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.height = height
        self.visitaMedica = False

    def info(self):
        print("L'atleta, ", self.name, self.surname, " di età ", self.age, ", pesa ", self.weight,"kg, ed è alto ", self.height, " cm")
        if self.visitaMedica == False:
            print("L'atleta ", self.name, self.surname, " non si è sottoposto alla visita medica ")
        else:
            print("L'atleta ", self.name, self.surname, " si è sottoposto alla visita medica")

    def effettua_visita(self):
        self.visitaMedica = True
        
    def squadra(self, team):
        self.team = team
        print("L'atleta gioca nella squadra ", self.team)

def main():
    name = input("Inserisci il nome dell'atleta ")
    surname = input("Inserisci il cognome dell'atleta ")
    age = input("Inserisci l'età dell'atleta ")
    weight = float(input("Inserisci il peso dell'atleta "))
    height = float(input("Inserisci l'altezza dell'atleta "))
    team = input("Inserisci la squadra in cui gioca l'atleta ")
    atleta = Atleta(name, surname, age, weight, height)
    visita = str(input("L'atleta si è sottoposto alla visita medica? "))
    if visita.upper == "SI":
        atleta.effettua_visita()
    atleta.info()
    atleta.squadra(team)

main()
