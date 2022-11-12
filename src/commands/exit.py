from src.commands.command_base import CommandBase

class CommandExit(CommandBase):
    def __init__(self, game_context):
        super(CommandExit, self).__init__(game_context, "exit", "Exits the game", ["e"]);
    
    def execute(self):
        print("Bis zum nächsten mal!")
        exit()