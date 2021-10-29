#from inheritance_5.players_and_monsters_3.project.knight import Knight
from project.knight import Knight


class BladeKnight(Knight):
    def __init__(self, username, level):
        Knight.__init__(self, username, level)


    def __repr__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"

