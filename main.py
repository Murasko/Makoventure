from src.creatures.player.player import Player
from src.map.map import Map
from src.commands import *


if __name__ == '__main__':
    name = input("Enter your name:\n> ")
    p = Player(name)
    m = Map()
    while True:
        command = input("> ").lower()
        match command:
            case "forward":
                move.forward(p, m)
            case "help":
                help.cli_help()
            case "attack":
                battle.attack(p, m.current_field)
            case "heal":
                p.heal()
            case "exit":
                print("Bis zum nächsten mal!")
                exit()
            case _:
                print("Unbekannte Eingabe!")
