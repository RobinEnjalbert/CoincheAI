# -*- coding: utf8 -*-

from src.Environment.Players.Player import Player


class Team:
    """
    A team is composed of two players and has a score.
    Attributes:
        players = list of two players
        score = team score
        won_cards = list of won cards during a single round
    """

    def __init__(self, player1, player2):
        assert isinstance(player1, Player), "[TEAM.PY] First player must be an object of type Player."
        assert isinstance(player2, Player), "[TEAM.PY] Second player must be an object of type Player."
        self.players = [player1, player2]
        self.__score = 0
        self.won_cards = []

    def get_score(self):
        return self.__score

    def add_score(self, points):
        if type(points) != int:
            raise TypeError("[TEAM.PY] Points must be type int.")
        if points < 0:
            raise ValueError("[TEAM.PY] Points must be positive.")
        self.__score += points

    def __str__(self):
        return "Players names: {}, {}\nScore: {}".format(self.players[0].get_name(), self.players[1].get_name(),
                                                         str(self.__score))

    def __repr__(self):
        return str(self)
