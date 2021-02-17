'''
Un'azienda vende prodotti in tutta Italia e la rete di vendita è suddivisa in quattro zone: Nord, Centro, Sud, Isole.
Dopo aver acquisito in un array il fatturato nelle quattro zone, calcola:
- il totale del fatturato;
- i valori in percentuale delle vendite nelle quattro zone rispetto al totale.
'''
zone = ["Nord", "Centro", "Sud", "Isole"]
fatturato_zone = []

for i in range(len(zone)): 
    fatturato = float(input("Inserisci il fatturato della zona " + zone[i] + " "))
    fatturato_zone.append(fatturato)
print("Il fatturato totale dell'azienda è ",sum(fatturato_zone))

for i in range(len(zone)):
    fatturato_percentuale = fatturato_zone[i]*100/sum(fatturato_zone)
    print("Il fatturato percentuale della zona ", zone[i], " è di ", fatturato_percentuale)