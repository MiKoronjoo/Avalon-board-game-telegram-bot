import game.characters.character as ch
import game.characters.evil as ev
import game.player as pl


class Merlin(ch.Character):
    def __init__(self, player: pl.Player):
        super().__init__(player, 'good')

    def get_evil(self):
        return [player for player in self.player.game.players if
                player.character.label == 'evil' and type(player.character) != ev.Mordred]


class Percival(ch.Character):
    def __init__(self, player: pl.Player):
        super().__init__(player, 'good')

    def get_merlin(self):
        return [player for player in self.player.game.players if
                type(player.character) in (Merlin, ev.Morgana)]


class Loyal(ch.Character):
    def __init__(self, player: pl.Player):
        super().__init__(player, 'good')
