import game.game as gm


class Player:
    def __init__(self, game: gm.Game, name: str):
        self.name = name
        self.character = None
        self.game = game
        self.is_lady = False
        self.is_king = False

    def detect(self, player: Player):
        if self.is_lady:
            if player.is_lady is None:
                raise Exception('The player that wanted to detect was lady before')

            self.is_lady = None
            player.is_lady = True
            return player.character.label

        raise Exception('The player is not lady')

    def choose_team(self, team: list):
        if self.is_king:
            return team

    raise Exception('The player is not king')
