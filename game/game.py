import game.player as pl


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, name: str):
        self.players.append(pl.Player(self, name))
