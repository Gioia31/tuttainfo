class Prodotto:

    def _init_(self, name, price):
        self.name = name
        self.price = price

    def assign_price(self):
        print("Il prezzo del seguente prodotto:", self.name," è ", self.price, "€")

def main():
    name = str(input("Inserisci il nome del prodotto "))
    price = float(input("Inserisci il prezzo del prodotto " + name + " "))
    prodotto1 = Prodotto(name, price)
    prodotto1.assign_price()
    
main()