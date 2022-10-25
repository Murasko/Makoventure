import random
from src.character.enemies.enemy import Enemy


def gen_random():
    rand = random.randint(0, 2)
    if rand == 0:
        return Field([Enemy("Gegner 1", 1)])
    elif rand == 1:
        return Field([Enemy("Gegner 2", 2)])
    else:
        return Field([Enemy("Gegner 3", 3)])


class Field:
    def __init__(self, enemies):
        self.enemies = enemies

    def print_state(self):
        print("You see ")
        for i in self.enemies:
            print(i.name)

