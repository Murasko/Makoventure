class Creature:
    def __init__(self):
        self.name = "Undefined Name"
        self.health = 10
        self.level = 1
        self.damage = 5

    def attack(self, enemy):
        print(f"Greife {self.name} mit {self.damage} an.")
        enemy.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} hat noch {self.health} Leben verbleibend")

    def level_up(self):
        pass
