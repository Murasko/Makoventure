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

import random


class Creature:
    def __init__(self):
        self.name = "Undefined Name"
        self._max_health = 0
        self._health = self._max_health
        self._damage = 0
        self._level = 1
        self._exp = 0
        self._is_dead = False
        self.is_player = False

# Properties / Getter & Setter

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, amount):
        self._level = amount

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, amount):
        self._exp = amount

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, amount):
        self._health = amount

    @property
    def max_health(self):
        return self._max_health

    @max_health.setter
    def max_health(self, amount):
        self._max_health = amount

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, amount):
        self._damage = amount

    @property
    def is_dead(self):
        return self._is_dead

    @is_dead.setter
    def is_dead(self, value):
        self._is_dead = value

# Functions

    def attack(self, enemy):
        enemy.health -= self.damage

    def heal(self):
        self.health = self.max_health

    def level_up(self):
        if random.randint(0, 1) == 0:
            self.max_health += 3
            self.level += 1
            self.heal()
            if self.is_player:
                print(f"Du wurdest geheilt und hast nun {self.health} Leben.")
        else:
            self.damage += 1
            self.level += 1
            if self.is_player:
                print(f"Du greifst nun mit {self.damage} Schaden an.")
