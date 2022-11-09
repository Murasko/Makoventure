import random


class Creature:
    def __init__(self):
        self.name = "Undefined Name"
        self._health = 10
        self._damage = 3
        self.level = 1
        self.is_dead = False

    @property
    def health(self):
        return self._health

    @property
    def damage(self):
        return self._damage

    def attack(self, enemy):
        print(f"{self.name} greift mit {self.damage} Schaden an.")
        enemy.take_damage(self.damage)

    def take_damage(self, damage):
        self._health -= damage
        if self.health <= 0:
            self.die()
        else:
            print(f"{self.name} hat noch {self.health} Leben.")

    def heal(self):
        self._health += 5
        print(f"{self.name} heilt sich und hat jetzt {self.health} Leben.")

    def level_up(self):
        level_up_attribute = random.randint(0, 1)
        if level_up_attribute == 0:
            self._health += 3
        else:
            self._damage += 1

    def die(self):
        print(f"{self.name} ist gestorben.")
        self.is_dead = True
