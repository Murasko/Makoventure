from src.creatures.enemies.enemy import Enemy

import random


class Map:
    def __init__(self):
        self.current_field = []

    def next(self):
        if len(self.current_field) > 0:
            print("Du kannst erst weiter gehen, wenn du alle Gegner besiegt hast.")
        else:
            enemy_amount = random.randint(1, 3)
            i = 0
            while i < enemy_amount:
                self.current_field.append(Enemy(f"Gegner {i + 1}", random.randint(2, 5)))
                i += 1
            for enemy in self.current_field:
                print(f"Du siehst {enemy.name} mit Level {enemy.level}.")
            return self.current_field

    def enemy_died(self, dead_enemy):
        self.current_field.pop(dead_enemy)
        return self.current_field
