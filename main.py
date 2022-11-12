from src.creatures.player.player import Player
from src.map.map import Map
from src.game_context import GameContext
from src.commands.command_handler import CommandHandler

def __print_license_banner():
    print("""Makoventure  Copyright (C) 2022  Marco Murawski
This program comes with ABSOLUTELY NO WARRANTY; for details type 'warranty' after naming your character.
This is free software, and you are welcome to redistribute it
under certain conditions; type 'license' for details after naming your character.""")

if __name__ == '__main__':
    __print_license_banner()
    print()

    name = input("Enter your name:\n> ")
    p = Player(name)
    m = Map()
    game_context = GameContext(p, m)
    command_handler = CommandHandler(game_context)
    print("Type 'help' to get help")
    command_handler.handle()