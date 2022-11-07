from src.creatures.enemies.enemy import Enemy


class Map:
    def __init__(self):
        self.current_field = []
        pass

    @property
    def field(self):
        return self.current_field

    @field.setter
    def field(self, enemy_amount):
        for i in range(1, enemy_amount):
            self.current_field.append(Enemy)
