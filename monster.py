class Entity: 
  def __init__(self, x, y, field):
    self.x = x
    self.y = y
    self.field = field
    self.field.entities.append(self) 

  def move(self, direction):
    if direction == "up":
      self.y -= 1
    elif direction == "down":
      self.y += 1
    elif direction == "left":
      self.x -= 1
    elif direction == "right":
      self.x += 1
      

class Monster(Entity):
  def __init__(self, x, y, name, damage, field):
    super().__init__(x, y, field)
    self.name = name
    self.hp = 10 #valore prestabilito
    self.damage = damage

  def info(self):
    print("Sono il mostro ", self.name)
    print("Hp: ", self.hp, "/10")
    print("Mi trovo alle coordinate ", self.x, self.y)

  def attack(self, enemy):
    if self.hp <= 0:
      print(self.name, "prova ad attaccare da morto con scarsi risultati")
    else: 
      print(self.name, "attacca", enemy.name)

      if (enemy.hp <= 0):
        print(enemy.name, "e' morto")
      else:
        enemy.hp -= self.damage


class Field:
  def __init__(self, w, h):
    self.w = w
    self.h = h
    self.entities = [] 

  def draw(self):
    print()
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if e.x >= self.w:
            e.x = self.w -1
          if e.y >= self.h:
            e.y = self.h -1
          if e.x <= 0:
            e.x = 0
          if e.y <= 0:
            e.y = 0
          if x == e.x and y == e.y:
            print("[x]", end = "")
            break    
        else:
          print("[ ]", end = "" )
      print()


field = Field(4,4)
m = Monster(2, 3, "Pino", 10, field)
m1 = Monster(0, 0, "Gino", 10, field)
m.info()
m1.info()
field.draw()
m1.attack(m)
m1.move("down")
field.draw()
m1.move("down")
field.draw()
m1.move("down")
field.draw()
m1.move("right")
field.draw()
m1.move("right")
field.draw()
