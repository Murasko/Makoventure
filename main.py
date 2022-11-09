from src.creatures.player.player import Player
from src.map.map import Map

if __name__ == '__main__':
    name = input("Enter your name:\n> ")
    p = Player(name)
    m = Map()
    while True:
        command = input("> ").lower()
        if command == "next":
            m.next()
        elif command == "help":
            print("""Command help:
help - Prints help
next - move to next field""")
        elif command == "attack":
            if not m.current_field:
                print("Keine Gegner zum angreifen.")
            else:
                for enemy in m.current_field:
                    p.attack(enemy)
                    if enemy.is_dead:
                        m.current_field.remove(enemy)
        else:
            print("Unbekannte Eingabe!")
