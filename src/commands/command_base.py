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

from abc import ABC, abstractmethod


class CommandBase(ABC):
    def __init__(self, game_context, name, description, aliases):
        self.game_context = game_context
        self.name = name
        self.description = description
        self.aliases = aliases
    
    @abstractmethod
    def execute(self):
        raise NotImplementedError("subclass must implement execute()!")
    
    # Wrapper methods for easier usage in subclasses
    def get_player(self):
        return self.game_context.player
    
    def get_world(self):
        return self.game_context.world
