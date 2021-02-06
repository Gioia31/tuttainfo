'''
I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario che ha per chiave la matricola, mentre il valore associato è il voto.
Elenca i risultati in ordine crescente di voto e successivamente visualizza quali voti diversi tra loro sono stati assegnati, riducendo a uno i voti uguali.
''' 
voti_studenti = {}
voti_diversi = []
contatore = 0

while True:
    contatore += 1
    print("Studente numero:",contatore)
    contatore += 1
    voto = float(input("Qual è il voto dello studente? "))
    voti_studenti[contatore] = voto

    if voto > 10:
        print("ATTENZIONE: i voti non possono superare il 10, ritenta!")
        contatore -= 1

    if contatore == 30:
        print("Elenco voti in ordine crescente")
        print(sorted(voti_studenti.values()))
        break
print()
for e in voti_studenti.values():
    if e not in voti_diversi:
        voti_diversi.append(e)
print(voti_diversi)