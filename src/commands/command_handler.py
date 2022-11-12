from src.commands.command_base import CommandBase
from src.commands.battle import CommandBattle
from src.commands.exit import CommandExit
from src.commands.heal import CommandHeal
from src.commands.help import CommandHelp
from src.commands.move import CommandMove

class CommandHandler:
    def __init__(self, game_context):
        self.game_context = game_context
        self.commands = []
        self.add_command(CommandBattle(self.game_context))
        self.add_command(CommandExit(self.game_context))
        self.add_command(CommandHeal(self.game_context))
        self.add_command(CommandHelp(self.game_context))
        self.add_command(CommandMove(self.game_context))
    
    def add_command(self, command):
        if any(c.isupper() for c in command.name):
            raise ValueError("Command %s has an uppercased character in its name." % command.name)
        for alias in command.aliases:
            if any(c.isupper() for c in alias):
                raise ValueError("Command %s has an uppercased character in its alias %s." % (command.name, alias))

        for cmd in self.commands:
            if command.name == cmd.name:
                raise ValueError("Tried adding command %s but its name is already used by command %s." % (command.name, cmd.name))
            if command.name in cmd.aliases:
                raise ValueError("Tried adding command %s but its name is already used as an alias of command %s." % (command.name, cmd.name))
            for alias in command.aliases:
                if alias == cmd.name:
                    raise ValueError("Tried adding command %s but its alias %s is already used by command %s." % (command.name, alias, cmd.name))
                if alias in cmd.aliases:
                    raise ValueError("Tried adding command %s but its alias %s is already used as an alias of command %s." % (command.name, alias, cmd.name))
        self.commands.append(command)
    
    def handle(self):
        while True:
            found = False
            cmd = input("> ").lower()
            for command in self.commands:
                if command.name == cmd or cmd in command.aliases:
                    found = True
                    command.execute()
                    break

            if not found:
                print("Unbekannte Eingabe!")