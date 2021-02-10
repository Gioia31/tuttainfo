'''
Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici. Fornito poi il nome della persona, il programma visualizza il suo numero di telefono oppure
un messaggio nel caso la persona non sia presente nella rubrica.
'''

rubrica = {
            "Carla" : 39486390549, 
            "Marco" : 89921894394, 
            "Giovanna" : 87930642136, 
            "Sara" : 903259045645, 
            "Luigi" : 934684635598,
}

nome = input("Dimmmi il nome della persona di cui vuoi sapere il numero di telfono")

if nome in rubrica : 
    print(rubrica[nome])
else: 
    print("Questo numero di telfono non è presente all'interno della rubrica")
    
