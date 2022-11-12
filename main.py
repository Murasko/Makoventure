from src.creatures.player.player import Player
from src.map.map import Map
from src.game_context import GameContext
from src.commands.command_handler import CommandHandler

if __name__ == '__main__':
    name = input("Enter your name:\n> ")
    p = Player(name)
    m = Map()
    game_context = GameContext(p, m)
    command_handler = CommandHandler(game_context)
    print("Type 'help' to get help")
    command_handler.handle()