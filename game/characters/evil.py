import game.characters.character as ch
import game.player as pl


class Mordred(ch.Character):
    def __init__(self, player: pl.Player):
        super().__init__(player, 'evil')


class Morgana(ch.Character):
    def __init__(self, player: pl.Player):
        super().__init__(player, 'evil')


class Oberon(ch.Character):
    def __init__(self, player: pl.Player):
        super().__init__(player, 'evil')


class Assassin(ch.Character):
    def __init__(self, player: pl.Player):
        super().__init__(player, 'evil')


class Minion(ch.Character):
    def __init__(self, player: pl.Player):
        super().__init__(player, 'evil')
