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
        super(CommandBattle, self).__init__(game_context, "battle", "Battles the current enemies", ["attack", "fight", "b", "a", "fi"])

    def execute(self):
        if not self.get_world().current_field:
            print("Keine Gegner zum angreifen.")
        else:
            for enemy in self.get_world().current_field:
                self.get_player().attack(enemy)
                if enemy.is_dead:
                    self.get_world().current_field.remove(enemy)
                    break
                print("")
                enemy.attack(self.get_player())
                print("")
                if self.get_player().is_dead:
                    print("Du bist leider gestorben, viel Glück beim nächsten mal.")
                    exit()
