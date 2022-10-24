from creatures.player.player import Player
from creatures.enemies.enemy import Enemy
from creatures.creature import Creature

p = Player("Player")
e = Enemy("Enemy")
c = Creature()


for i in range(10):
    p.level_up()
    print(p.health, p.damage)
