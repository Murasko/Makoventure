from src.creatures.creature import Creature


class Player(Creature):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._max_health = 15
        self._health = self._max_health
        self._damage = 5

