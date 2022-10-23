class Creature:
    def __init__(self, health, level, damage):
        self.health = health
        self.level = level
        self.damage = damage

    def attack(self, enemy):
        enemy.take_damage(self.damage)

    def take_damage(self, damage):
        pass

    def level_up(self):
        pass
