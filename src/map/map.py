from src.creatures.enemies.enemy import Enemy
import random


class Map:
    def __init__(self):
        self.level = 1
        self.current_field = []

    def next(self, player):
        if len(self.current_field) > 0:
            print("Du kannst erst weiter gehen, wenn du alle Gegner besiegt hast.")
        else:
            enemy_amount = random.randint(1, int(self.level))
            i = 0
            while i < enemy_amount:
                self.current_field.append(Enemy(f"Gegner {i + 1}", random.randint(player.level, player.level + 2)))
                i += 1
            for enemy in self.current_field:
                print(f"Du siehst {enemy.name} mit Level {enemy.level}.")
            self.level += 0.5
            return self.current_field
