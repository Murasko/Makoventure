from creatures.player.player import Player
from creatures.enemies.enemy import Enemy

p = Player(Player)
e = Enemy(Enemy)

print(e.health)
p.attack(e)
p.attack(e)