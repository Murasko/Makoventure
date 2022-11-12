from src.commands.command_base import CommandBase

class CommandBattle(CommandBase):
    def __init__(self, game_context):
        super(CommandBattle, self).__init__(game_context, "battle", "Battles the current enemies", ["attack", "fight", "b", "a", "fi"])

    def execute(self):
        if not self._get_map().current_field:
            print("Keine Gegner zum angreifen.")
        else:
            for enemy in self._get_map().current_field:
                self._get_player().attack(enemy)
                if enemy.is_dead:
                    self._get_map().current_field.remove(enemy)
                    break
                print("")
                enemy.attack(self._get_player())
                print("")
                if self._get_player().is_dead:
                    print("Du bist leider gestorben, viel Glück beim nächsten mal.")
                    exit()