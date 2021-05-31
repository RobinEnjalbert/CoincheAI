# -*- coding: utf8 -*-

from src.Environment.Hand import Hand


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

    def set_type(self, type):
        self.__type = type

    def choose_bidding(self, bidding, bidding_history):
        raise NotImplementedError

    def __str__(self):
        return "Player name: {}\nPlayer hand: {}".format(self.__name, str(self.hand))

    def __repr__(self):
        return str(self)
