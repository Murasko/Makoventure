#      Makoventure - A basic Textadventure
#      Copyright (C) 2022 Marco Murawski
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#      Contact:
#      info@murasko.de

from src.creatures.enemies.enemy import Enemy
import random


class World:
    def __init__(self):
        self.level = 1
        self.current_field = []

    def forward(self, player):
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
