from src.creatures.creature import Creature


class Player(Creature):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run_away(self):
        print("Running!")

    def meditate(self):
        print("Du setzt dich entspannt hin und beginnst zu meditieren...")
        self.__health += 5
