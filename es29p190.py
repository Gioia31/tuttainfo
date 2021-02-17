'''
Nella maggior parte dei sistemi fiscali la tassazione dei redditi avvine con aliquote progressive ( o a scagliono di reddito). 
Scrivi un programma che legga un reddito da tastiera e colacoli l'imposrto sul reddito e la tassazione media. 
'''
reddito = int(input("Inserisci il tuo reddito "))

if reddito <= 15000:
    imposta = 0.23 * reddito
    tassazione_media = imposta/reddito * 100
    print("L'importo dell'imposta sul reddito è ",imposta, " € ")
    print("La tassazione media è ", tassazione_media, " %")

elif 15000 < reddito <= 28000:
    imposta = 3450+0.27*(reddito-15000)
    tassazione_media = imposta/reddito * 100
    print("L'importo dell'imposta sul reddito è ",imposta, " € ")
    print("La tassazione media è ", tassazione_media, " %")

elif 28000 < reddito <= 55000:
    imposta = 3450 + 3510 + 0.38*(reddito-28000)
    tassazione_media = imposta/reddito * 100
    print("L'importo dell'imposta sul reddito è ",imposta, " € ")
    print("La tassazione media è ", tassazione_media, " %")

elif 55000 < reddito <= 75000:
    imposta = 3450 + 3510 + 10260+ 0.41 *(reddito - 55000)
    tassazione_media = imposta/reddito *100
    print("L'importo dell'imposta sul reddito è ",imposta, " € ")
    print("La tassazione media è ", tassazione_media, " %")

else:
    imposta = 3450 + 3510 + 10260 + 8200 + 0.43*(reddito-75000)
    tassazione_media = imposta/reddito *100
    print("L'importo dell'imposta sul reddito è ",imposta, " € ")
    print("La tassazione media è ", tassazione_media, " %")