from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        try:                                                                          # vij card_repository za drugo reshenie na add metoda
            player = [p for p in self.players if p.username == player.username][0]
            raise ValueError(f"Player {player.username} already exists!")
        except:
            self.players.append(player)
            self.count += 1

                     # player = player.username zashtoto e str
    def remove(self, player: str):
        if player == '':
            raise ValueError("Player cannot be an empty string!")
        player = [p for p in self.players if p.username == player][0]
        self.players.remove(player)
        self.count -= 1

    def find(self, username: str):
        player = [p for p in self.players if p.username == username][0]
        return player