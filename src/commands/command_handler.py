#      Makoventure - A basic Textadventure
#      Copyright (C) 2022 Marco Murawski
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#      Contact:
#      info@murasko.de

from src.commands.battle import CommandBattle
from src.commands.exit import CommandExit
from src.commands.heal import CommandHeal
from src.commands.help import CommandHelp
from src.commands.license import CommandLicense
from src.commands.move import CommandMove
from src.commands.warranty import CommandWarranty


class CommandHandler:
    def __init__(self, game_context):
        self.game_context = game_context
        self.commands = []
        self.add_command(CommandBattle(self.game_context))
        self.add_command(CommandExit(self.game_context))
        self.add_command(CommandHeal(self.game_context))
        self.add_command(CommandHelp(self.game_context))
        self.add_command(CommandLicense(self.game_context))
        self.add_command(CommandMove(self.game_context))
        self.add_command(CommandWarranty(self.game_context))
    
    def add_command(self, command):
        if any(c.isupper() for c in command.name):
            raise ValueError(f"Command {command.name} has an uppercase character in its name.")
        for alias in command.aliases:
            if any(c.isupper() for c in alias):
                raise ValueError(f"Command {command.name} has an uppercase character in its alias {alias}.")

        for registered_command in self.commands:
            if command.name == registered_command.name:
                raise ValueError(f"Tried adding command {command.name} but its name is already used by command {registered_command.name}.")
            if command.name in registered_command.aliases:
                raise ValueError(f"Tried adding command {command.name} but its name is already used as an alias of command {registered_command.name}.")
            for alias in command.aliases:
                if alias == registered_command.name:
                    raise ValueError(f"Tried adding command {command.name} but its alias {alias} is already used by command {registered_command.name}.")
                if alias in registered_command.aliases:
                    raise ValueError(f"Tried adding command {command.name} but its alias {alias} is already used as an alias of command {registered_command.name}.")
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
