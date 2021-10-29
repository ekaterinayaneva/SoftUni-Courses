#from inheritance_5.players_and_monsters_3.project.hero import Hero
from project.hero import Hero


class Wizard(Hero):
    def __init__(self, username, level):
        Hero.__init__(self, username, level)

    def __repr__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"


