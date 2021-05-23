import numpy as np
from .constants import STRENGTH, CARD_COLORS, TRUMPS
from .Card import Card


class Hand:

    def __init__(self, cards):
        if not isinstance(cards, list) or not isinstance(cards[0], Card):
            raise TypeError("[HAND.PY] The hand must be a list of Cards")
        if len(cards) != 8:
            raise ValueError("[HAND.PY] The given hand has {} cards while 8 are required.".format(len(cards)))
        self.__hand = cards
        self.__available = [i for i in range(8)]

    def reset(self, cards):
        self.__hand = cards
        self.__available = [i for i in range(8)]

    def sort(self, trump='NT'):
        if trump not in TRUMPS:
            raise ValueError("[HAND.PY] Given trump '{}' to sort hand does not exist.".format(trump))
        sorted_hand = []
        # Sort by color
        color_sort = {CARD_COLORS[0]: [],
                      CARD_COLORS[1]: [],
                      CARD_COLORS[2]: [],
                      CARD_COLORS[3]: []}
        for card in self.__hand:
            color = CARD_COLORS[card.getColor()]
            color_sort[color].append(card)
        # Sort each color by value
        for k in color_sort.keys():
            color = color_sort[k]
            strength = STRENGTH['basic'] if k != trump else STRENGTH['trump']
            color_strength = [strength[card.getValue()] for card in color]
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

    def get(self):
        hand = np.array(self.__hand)
        return hand[self.__available]

    def __str__(self):
        return str(self.get())

    def __repr__(self):
        return str(self.get())
