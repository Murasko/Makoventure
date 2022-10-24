from creatures.creature import Creature


class Enemy(Creature):
    def __init__(self, name):
        super().__init__()
        self.name = name


    