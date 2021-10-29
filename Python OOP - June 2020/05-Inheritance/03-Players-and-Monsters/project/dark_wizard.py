#from inheritance_5.players_and_monsters_3.project.wizard import Wizard
from project.wizard import Wizard


class DarkWizard(Wizard):
    def __init__(self, username, level):
        Wizard.__init__(self, username, level)


    def __repr__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"

