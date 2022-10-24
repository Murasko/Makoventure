from creatures.creature import Creature

class Enemy(Creature):
    def __init__(self, name):
        self.name = name
        super().__init__()

    