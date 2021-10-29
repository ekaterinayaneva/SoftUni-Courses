class Guild:
    def __init__(self, guild_name):
        self.guild_name = [guild_name] = []
        self.list_of_players = []


    def assign_player(self, player: Player):
        if player in self.guild_name:
            return f"Player {player} is already in the guild"

        self.guild_name += player
        return f"Welcome player {player} to the guild {self.guild_name}"

    