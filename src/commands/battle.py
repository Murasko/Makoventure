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


from src.commands.command_base import CommandBase


class CommandBattle(CommandBase):
    def __init__(self, game_context):
        super().__init__(game_context, "battle", "Battles the current enemies", ["attack", "fight", "b", "a", "fi"])

    def execute(self):
        world = self.get_world()
        field = world.current_field
        dead_enemies = world.dead_enemies
        player = self.get_player()
        if not field:
            print("Keine Gegner zum angreifen.")
        else:
            for enemy in field:
                enemy.attack(player)
                self.check_health(player, field)

            for enemy in field:
                player.attack(enemy)
                self.check_health(enemy, field)
            self.print_battle_state(field, player)
            self.get_exp(dead_enemies, player)
            self.check_levelup(player)

    def enemy_died(self, field, enemy):
        field.remove(enemy)

    def check_health(self, creature, field):
        if creature.health <= 0 and creature.is_player:
            print("Du bist leider gestorben. Viel Erfolg beim nächsten mal!")
            exit()
        elif creature.health <= 0:
            self.enemy_died(field, creature)
            print(f"{creature.name} wurde getötet.")

    def print_battle_state(self, field, player):
        for creature in field:
            print(f"{creature.name}: {creature.health} HP verbleibend.")
        print()
        print(f"{player.name}: {player.health} HP verbleibend.")

    def get_exp(self, dead_enemies, player):
        for _ in range(dead_enemies):
            player.exp += 4

    def check_levelup(self, player):
        if player.exp >= 10:
            player.level_up()
            player.exp -= 10

