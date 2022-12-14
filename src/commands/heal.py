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


class CommandHeal(CommandBase):
    def __init__(self, game_context):
        super().__init__(game_context, "heal", "Heals the player", ["restore", "rest", "h", "r"])

    def execute(self):
        player = self.get_player()
        player.heal()
        if player.is_player:
            print(f"Du wurdest geheilt und hast nun wieder {player.health} Leben.")
