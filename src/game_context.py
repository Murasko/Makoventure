from src.creatures.player.player import Player
from src.map.map import Map

class GameContext:
    def __init__(self, player, map):
        self.player = player
        self.map = map