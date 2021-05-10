# -*- coding: utf8 -*-

import random
from Card import Card


class Deck:
    """
    Deck class: A deck is composed of 32 different Cards.
    Attributes:
        cardList = [32 cards list]
    """

    def __init__(self):
        self.cardList = [Card(v_idx, c_idx) for c_idx in range(4) for v_idx in range(8)]

    def shuffle(self):
        random.shuffle(self.cardList)

    def cut(self):
        cut = random.randint(2, 29)
        self.cardList = self.cardList[cut:] + self.cardList[:cut]

    def distribute(self, two=1):
        if two not in range(3):
            raise ValueError("[DECK.PY] Two must be an index in [0:2].")
        sequence = [3, 3, 3]
        sequence[two] = 2
        hands = [[] for _ in range(4)]
        for nb_cards in sequence:
            for hand in hands:
                hand += self.cardList[:nb_cards]
                self.cardList = self.cardList[nb_cards:]
        return hands

    def __str__(self):
        s = ""
        for card in self.cardList:
            s += str(card) + "\n"
        return s

    def __repr__(self):
        s = ""
        for card in self.cardList:
            s += str(card) + "\n"
        return s
