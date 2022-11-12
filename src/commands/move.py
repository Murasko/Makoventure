from src.commands.command_base import CommandBase

class CommandMove(CommandBase):
    def __init__(self, game_context):
        super(CommandMove, self).__init__(game_context, "move", "Moves forward on the map", ["forward", "next", "m", "fo", "n"])
    
    def execute(self):
        self._get_map().forward(self._get_player())