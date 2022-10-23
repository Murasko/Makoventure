from creatures.creature import Creature


class Player(Creature):
    def __init__(self):
        super().__init__()

    def run_away(self):
        print("Running!")

    def meditate(self):
        pass
