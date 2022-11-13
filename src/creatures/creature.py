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
        self._max_health = 10
        self._health = self._max_health
        self._damage = 3
        self._level = 1
        self._exp = 0
        self.is_dead = False

    @property
    def lvl(self):
        return self._level

    @lvl.setter
    def lvl(self, amount):
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

    def attack(self, enemy):
        print(f"{self.name} greift mit {self.damage} Schaden an.")
        enemy.take_damage(self.damage)
        if enemy.is_dead:
            self.exp += 2
        if self.exp >= 10:
            self.level_up(True)
            self.exp = 0
            return self._exp

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()
        else:
            print(f"{self.name} hat noch {self.health} Leben.")

    def heal(self, amount=5):
        if self.health == self.max_health:
            print("Du bist bereits vollständig geheilt.")
        elif self.health + amount > self.max_health:
            self.health = self.max_health
            print(f"{self.name} heilt sich und hat jetzt {self.health} Leben.")
        else:
            self.health += amount
            print(f"{self.name} heilt sich und hat jetzt {self.health} Leben.")

    def level_up(self, player=False):
        level_up_attribute = random.randint(0, 1)
        if level_up_attribute == 0:
            self.max_health += 3
            if player:
                print(f"Du bist aufgestiegen und hast nun maximal {self.max_health} Leben.")
                self.lvl += 1
        else:
            self.damage += 1
            if player:
                print(f"Du bist aufgestiegen und hast nun {self.damage} Schaden.")
                self.lvl += 1

    def die(self):
        print(f"{self.name} ist gestorben.")
        self.is_dead = True
