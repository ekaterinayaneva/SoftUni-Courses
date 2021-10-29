#from inheritance_5.players_and_monsters_3.project.elf import Elf
from project.elf import Elf


class MuseElf(Elf):
    def __init__(self, username, level):
        Elf.__init__(self, username, level)

    def __repr__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"

