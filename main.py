from src.character.player.player import Player
from src.character.enemies.enemy import Enemy
from src.map.map import Map

p = Player("Player")
e = Enemy("Enemy", 3)

print(e.health)
p.attack(e)
"""for i in range(10):
    p.level_up()
    print(p.health, p.damage)"""

if __name__ == '__main__':
    name = input("Enter your name")
    p = Player(name)
    current_map = Map(5, 5)
    while True:
        command = input(">").lower()
        Commands[command[0]](p, map)
        current_map.map()
