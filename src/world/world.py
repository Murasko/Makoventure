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
        self.stage = 1
        self.current_field = []

    def is_field_empty(self):
        if len(self.current_field) > 0:
            return False
        else:
            return True

    def generate_enemies(self, p_lvl):
        enemy_amount = random.randint(1, int(self.stage))
        while len(self.current_field) < enemy_amount:
            enemy_level = random.randint(p_lvl, p_lvl + 2)
            self.current_field.append(Enemy(f"Gegner {len(self.current_field) + 1 }", enemy_level))
        self.stage += 0.4

    def print_field(self):
        for enemy in self.current_field:
            print(f"{enemy.name} - LVL: {enemy.level}, HP: {enemy.health}, DMG: {enemy.damage}")

    def move(self, player):
        if self.is_field_empty():
            self.generate_enemies(player.level)
            print("Du gehst weiter und siehst:")
            self.print_field()
        else:
            print("Du musst dir erst den Weg frei kämpfen")
