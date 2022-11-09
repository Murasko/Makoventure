from src.creatures.player.player import Player
from src.map.map import Map
from src.constants.help import cli_help

if __name__ == '__main__':
    name = input("Enter your name:\n> ")
    p = Player(name)
    m = Map()
    while True:
        command = input("> ").lower()
        match command:
            case "next":
                m.next(p)
            case "help":
                cli_help()
            case "attack":
                if not m.current_field:
                    print("Keine Gegner zum angreifen.")
                else:
                    for enemy in m.current_field:
                        p.attack(enemy)
                        if enemy.is_dead:
                            m.current_field.remove(enemy)
                        print("")
                        enemy.attack(p)
                        if p.is_dead:
                            print("Du bist leider gestorben, viel Glück beim nächsten mal.")
                            exit()
            case "exit":
                print("Bis zum nächsten mal!")
                exit()
            case _:
                print("Unbekannte Eingabe!")
