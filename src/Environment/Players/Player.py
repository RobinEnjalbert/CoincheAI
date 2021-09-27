# -*- coding: utf8 -*-

from src.Environment.Materials.Hand import Hand


class Player:
    """
    Base class for players.
    A player has a name and a hand.
    Attributes:
        name = identifier
        type = player type (human, random or AI)
        hand = list of 8 cards with list of available cards
    """

    def __init__(self, name, index):
        if type(name) != str:
            raise TypeError("[PLAYER.PY] Name must be type str.")
        if type(index) != int:
            raise TypeError("[PLAYER.PY] Index must be type int.")
        self.__name = name
        self.__index = index
        self.__type = None
        self.hand = Hand()

    def get_name(self):
        return self.__name

    def get_index(self):
        return self.__index

    def get_type(self):
        return self.__type

    def set_type(self, type_name):
        if type_name not in ['AI', 'Human', 'Random']:
            raise ValueError(f"[PLAYER.PY] Wrong type '{type_name}' for player.")
        self.__type = type

    def choose_bidding(self, bidding, bidding_history):
        raise NotImplementedError

    def __str__(self):
        return f"Player name: {self.__name}\nPlayer hand: {str(self.hand)}"

    def __repr__(self):
        return str(self)
