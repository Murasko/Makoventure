from src.commands.command_base import CommandBase

class CommandHeal(CommandBase):
    def __init__(self, game_context):
        super(CommandHeal, self).__init__(game_context, "heal", "Heals the player", ["restore", "rest", "h", "r"])
    
# TODO: Dynamic output
    def execute(self):
        self._get_player().heal()