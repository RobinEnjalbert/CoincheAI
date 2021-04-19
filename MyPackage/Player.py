# -*- coding: utf8 -*-

class Player:
    """
    Player class: A player has a name and a hand.
    Attributes:
        name = player's name
        cardList = [32 cards list]
    """

    def __init__(self, name):
        if type(name) != str:
            raise TypeError("[PLAYER.PY] Name must be type str.")
        self.name = name
        self.hand = []
