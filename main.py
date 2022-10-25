from src.character.player.player import Player
from src.map.map import Map
from src.map.field import Field

if __name__ == '__main__':
    name = input("Enter your name ")
    p = Player(name)
    current_map = Map(5, 5)
    while True:
        command = input("> ").lower()
        if command == "right":
            current_map.move_right()
        elif command == "forward":
            current_map.move_forward()
        elif command == "attack":
            p.attack(current_map.enemies)
        current_map.map
