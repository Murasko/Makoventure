import random


class Creature:
    def __init__(self):
        self.name = "Undefined Name"
        self.__health = 10
        self.__damage = 5
        self.level = 1

    @property
    def health(self):
        return self.__health

    @property
    def damage(self):
        return self.__damage

    def attack(self, enemy):
        for e in enemy:
            print(f"{self.name} greift mit {self.damage} Schaden an.")
            e.take_damage(self.damage)

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            self.die()
        else:
            print(f"{self.name} hat noch {self.__health} Leben.")

    def level_up(self):
        level_up_attribute = random.randint(0, 1)
        if level_up_attribute == 0:
            self.__health += 3
        else:
            self.__damage += 1

    def die(self):
        print(f"{self.name} ist gestorben.")
