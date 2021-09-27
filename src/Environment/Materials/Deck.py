# -*- coding: utf8 -*-

import random
from src.Environment.Materials.Card import Card


class Deck:
    """
    A deck is composed of all 32 cards and is used for distribution.
    Attributes:
        cards = list of the 32 cards
    Methods:
        shuffle() -> Shuffle the deck
        cut() -> Cut the deck
        distribute(two) -> Distribute the deck in 4 hands; two tells if the distribution is either 332, 323 or 233
        reset(cards) -> Reset the deck with collected cards
        str(), repr()
    """

    def __init__(self):
        self.__cards = [Card(v_idx, c_idx) for c_idx in range(4) for v_idx in range(8)]

    def shuffle(self):
        random.shuffle(self.__cards)

    def cut(self):
        cut = random.randint(2, 29)
        self.__cards = self.__cards[cut:] + self.__cards[:cut]

    def distribute(self, two=1):
        if two not in range(3):
            raise ValueError("[DECK.PY] Two must be an index in [0:2].")
        sequence = [3, 3, 3]
        sequence[two] = 2
        hands = [[] for _ in range(4)]
        for nb_cards in sequence:
            for hand in hands:
                hand += self.__cards[:nb_cards]
                self.__cards = self.__cards[nb_cards:]
        return hands

    def reset(self, cards):
        self.__cards = cards

    def __str__(self):
        s = ""
        for card in self.__cards:
            s += str(card) + "\n"
        return s

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.__cards)
