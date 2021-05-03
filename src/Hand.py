from .constants import STRENGTH, CARD_COLORS
from .Card import Card


class Hand:

    def __init__(self, cards):
        if not isinstance(cards, list) or not isinstance(cards[0], Card):
            raise TypeError("[HAND.PY] The hand must be a list of Cards")
        if len(cards) != 8:
            raise ValueError("[HAND.PY] The given hand has {} cards while 8 are required.".format(len(cards)))
        self.hand = cards
        self.played = [1 for _ in range(8)]

    def sort(self, trump):
        if trump not in CARD_COLORS:
            raise ValueError("[HAND.PY] Given trump '{}' to sort hand does not exist.".format(trump))
        sorted_hand = []
        # Sort by color
        color_sort = {CARD_COLORS[0]: [],
                      CARD_COLORS[1]: [],
                      CARD_COLORS[2]: [],
                      CARD_COLORS[3]: []}
        for card in self.hand:
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
        self.hand = sorted_hand

    def play(self, idx):
        if idx not in range(8):
            raise ValueError("[HAND.PY] Idx must be in [0:7].")
        self.played[idx] = 0

    def __str__(self):
        return str(self.hand)

    def __repr__(self):
        return str(self.hand)
