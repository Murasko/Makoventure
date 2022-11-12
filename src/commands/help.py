from src.commands.command_base import CommandBase

class CommandHelp(CommandBase):
    def __init__(self, game_context):
        super(CommandHelp, self).__init__(game_context, "help", "Prints available commands for the player", ["info", "?", "-h"])
    
# TODO: Dynamic output
    def execute(self):
        print("""Command help:
help    -   prints help
forward -   move forward to next field
attack  -   execute one attack round
heal    -   heal 5 health
exit    -   close the game""")