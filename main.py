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

from src.creatures.player.player import Player
from src.world.world import World
from src.game_context import GameContext
from src.commands.command_handler import CommandHandler


def print_license_banner():
    print("""    Makoventure  Copyright (C) 2022  Marco Murawski
    This program comes with ABSOLUTELY NO WARRANTY; for details type 'warranty'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type 'license' for details.""")


if __name__ == '__main__':
    print_license_banner()
    print()

    print("Type 'help' to get help")
    print()

    name = input("Enter your name:\n> ")
    player = Player(name)
    world = World()
    game_context = GameContext(player, world)
    command_handler = CommandHandler(game_context)
    command_handler.handle()
