class Monster:
    def __init__ (self, nome, demage):
        self.nome = nome
        self.hp = 10
        self.demage = demage
    
    def info(self):
        print("sono ", self.nome)
    
    def attack (self, enemy):
        print(self.nome, " attacca ", enemy.nome)

        if (enemy.hp <= 0):
            print(enemy.nome, " è morto")
        else:
            enemy.hp -= self.demage


m1 = Monster("Pino", 6)
m1.info()

m2 = Monster("Pluto", 2)
m2.info()

m1.attack(m2)
m1.attack(m2)
m1.attack(m2)
