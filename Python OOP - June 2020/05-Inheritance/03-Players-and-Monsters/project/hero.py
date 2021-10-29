class Hero:
    def __init__(self, username, level):
        self.level = level
        self.username = username

    def __repr__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"

