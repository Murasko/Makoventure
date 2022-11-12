from abc import abstractmethod

class CommandBase:
    def __init__(self, game_context, name, description, aliases):
        self.game_context = game_context
        self.name = name
        self.description = description
        self.aliases = aliases
    
    @abstractmethod
    def execute(self):
        raise NotImplementedError('subclasse must implement execute()!')
    
    # Wrapper methods for easier usage in subclasses
    def _get_player(self):
        return self.game_context.player
    
    def _get_map(self):
        return self.game_context.map