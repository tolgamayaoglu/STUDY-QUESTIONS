class House():
    def __init__(self, sigil, motto):
        self.sigil = sigil
        self.motto = motto
        self.allies = []
        self.enemies = []
    
    def speak(self):
        return self.motto
    
    def show(self):
        return self.sigil

    def set_motto(self, motto):
        self.motto = motto

    def set_sigil(self, sigil):
        self.sigil = sigil

    def __str__(self):
        return 'Our Sigil is a ' + self.show() + ' and our motto is "' + self.speak() + '"'
    
    def add_to_allies(self, other):
        if other not in self.allies:
            self.allies.append(other)
    
    def remove_from_allies(self, other):
        if other in self.allies:
            self.allies.remove(other)
    
    def get_allies(self):
        return self.allies[:]

    def add_to_enemies(self, other):
        if other not in self.enemies:
            self.enemies.append(other)
    
    def remove_from_enemies(self, other):
        if other in self.enemies:
            self.enemies.remove(other)

    def get_enemies(self):
        return self.enemies[:]

    def make_an_alliance(self, other):
        self.remove_from_enemies(other)
        self.add_to_allies(other)
        other.remove_from_enemies(self)
        other.add_to_allies(self)
    
    def go_to_war(self, other):
        self.remove_from_allies(other)
        self.add_to_enemies(other)
        other.remove_from_allies(self)
        other.add_to_enemies(self)

Stark = House('direwolf', 'Winter Is Coming')
Arryn = House('falcon', 'As High As Honour')
Lannister = House('golden lion', 'Hear Me Roar')
Targaryen = House('three-headed dragon', 'Fire And Blood')
Greyjoy = House('golden kraken', 'We Do Not Sow')
Baratheon = House('crowned black stag', 'Ours Is The Fury')
Martel = House('red sun pierced by a golden spear', 'Unbowed, Unbent, Unbroken')
Tully = House('silver trout', 'Family, Duty, Honour')
Tyrel = House('golden rose', 'Growing Strong')

houses = [Stark, Arryn, Lannister, Targaryen, Greyjoy, Baratheon, Martel, Tully, Tyrel]
def state_of_westeros(houses):
    for house in houses:
        print(house)
        print("Our Allies Are: ")
        for ally in house.get_allies():
            print(ally)
        print("Our Enemies Are: ")
        for enemy in house.get_enemies():
            print(enemy)
        print("-----------------------")

Stark.make_an_alliance(Tully)
Stark.make_an_alliance(Arryn)
print("First:")
state_of_westeros(houses)
Tully.go_to_war(Stark)
print("Then:")
state_of_westeros(houses)