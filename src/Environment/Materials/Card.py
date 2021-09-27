# -*- coding: utf8 -*-

from src.Environment.constants import CARD_VALUES, CARD_COLORS


class Card:
    """
    A card has a value and a color.
    Attributes:
        value = CARD_VALUES[index] with index in range [0,7]
        color = CARD_COLORS[index] with index in range [0,3]
    Methods:
        get_value() -> card value
        get_color() -> card color
        str(), repr(), eq(), ne()
    """

    def __init__(self, value_idx, color_idx):
        if type(value_idx) != int:
            raise AssertionError("[CARD.PY] Value index must be type int.")
        if type(color_idx) != int:
            raise AssertionError("[CARD.PY] Color index must be type int.")
        if value_idx not in range(8):
            raise ValueError("[CARD.PY] Value index must be in [0,7].")
        if color_idx not in range(4):
            raise ValueError("[CARD.PY] Color index must be in [0,3].")
        self.__value = value_idx
        self.__color = color_idx

    def get_value(self):
        return self.__value

    def get_color(self):
        return self.__color

    def __str__(self):
        return "{} of {}".format(CARD_VALUES[self.__value],
                                 CARD_COLORS[self.__color])

    def __repr__(self):
        return str(self)

    def __eq__(self, card):
        assert isinstance(card, Card), "[CARD.PY] The card must be an object of type Card."
        same_value = self.__color == card.__color
        same_color = self.__value == card.__value
        return same_value and same_color

    def __ne__(self, card):
        assert isinstance(card, Card), "[CARD.PY] The card must be an object of type Card."
        return not (self.__eq__(card))
