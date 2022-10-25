from src.character.character import Creature


class Enemy(Creature):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        if self.level != 1:
            for i in range(1, self.level):
                self.level_up()
