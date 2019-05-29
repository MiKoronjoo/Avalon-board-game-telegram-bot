import game.player as pl


class Character:
    def __init__(self, player: pl.Player, label: str):
        if type(label) != str:
            raise TypeError("Type of 'label' must be 'str'")

        if label not in ('evil', 'good'):
            raise ValueError("'label' must be 'evil' or 'good'")

        self.label = label
        self.player = player
