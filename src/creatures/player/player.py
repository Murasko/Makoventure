from src.creatures.creature import Creature


class Player(Creature):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._health = 15
        self._damage = 5
