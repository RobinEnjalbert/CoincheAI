# -*- coding: utf8 -*-

import numpy as np
from src.Environment.constants import STRENGTH, CARD_COLORS, TRUMPS
from src.Environment.Materials.Card import Card


class Hand:
    """
        A hand is composed of the 8 cards given to a player.
        Attributes:
            hand = list of 8 cards
            available = list of not played cards indices
        Methods:
            set() -> Give a new hand
            get() -> Get the list of cards still in hand
            sort(trump) -> Sort the hand according to the actual trump
            play(idx) -> Update the not played cards list
            str(), repr()
        """

    def __init__(self):
        self.__hand = []
        self.__available = [i for i in range(8)]

    def set(self, cards):
        if not isinstance(cards, list) or not isinstance(cards[0], Card):
            raise TypeError("[HAND.PY] The hand must be a list of Cards")
        if len(cards) != 8:
            raise ValueError("[HAND.PY] The given hand has {} cards while 8 are required.".format(len(cards)))
        self.__hand = cards
        self.__available = [i for i in range(8)]

    def get(self, full=False):
        if full:
            return self.__hand
        else:
            hand = np.array(self.__hand)
            return hand[self.__available].tolist()

    def sort(self, trump=5):
        if trump not in range(len(TRUMPS)):
            raise ValueError("[HAND.PY] Given trump index '{}' to sort hand does not exist.".format(trump))
        sorted_hand = []
        # Sort by color
        color_sort = {CARD_COLORS[0]: [], CARD_COLORS[1]: [], CARD_COLORS[2]: [], CARD_COLORS[3]: []}
        for card in self.__hand:
            color = CARD_COLORS[card.get_color()]
            color_sort[color].append(card)
        # Sort each color by value
        for k in color_sort.keys():
            color = color_sort[k]
            strength = STRENGTH['basic'] if k != TRUMPS[trump] else STRENGTH['trump']
            color_strength = [strength[card.get_value()] for card in color]
            for _ in range(len(color)):
                idx = color_strength.index(min(color_strength))
                sorted_hand.append(color[idx])
                color.remove(color[idx])
                color_strength.remove(color_strength[idx])
        self.__hand = sorted_hand

    def play(self, idx):
        if idx not in range(8):
            raise ValueError("[HAND.PY] Idx must be in [0:7].")
        self.__available.remove(self.__available[idx])

    def __str__(self):
        return str(self.get())

    def __repr__(self):
        return str(self)
