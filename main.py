from src.creatures.player.player import Player

if __name__ == '__main__':
    name = input("Enter your name:\n> ")
    p = Player(name)
    while True:
        command = input("> ").lower()
        if command == "forward":
            pass
        elif command == "attack":
            pass
