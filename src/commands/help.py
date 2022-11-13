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


class CommandHelp(CommandBase):
    def __init__(self, game_context):
        super(CommandHelp, self).__init__(game_context, "help", "Prints available commands for the player", ["info", "?", "-h"])
    
# TODO: Dynamic output
    def execute(self):
        print("""Command help:
help    -   prints help
forward -   move forward to next field
attack  -   execute one attack round
heal    -   heal 5 health
exit    -   close the game""")
