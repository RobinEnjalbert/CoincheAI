# -*- coding: utf8 -*-

from .Player import Player


class Team:
    """
    Team class: A team is composed of two players and has a score.
    Attributes:
        players = [list of two players]
        score = team score
    """

    def __init__(self, player1, player2):
        assert isinstance(player1, Player), "[TEAM.PY] First player must be an object of type Player."
        assert isinstance(player2, Player), "[TEAM.PY] Second player must be an object of type Player."
        self.players = [player1, player2]
        self.score = 0

    def addPoints(self, points):
        """ Add points to the team's score """
        if type(points) != int:
            raise TypeError("[TEAM.PY] Points must be type int.")
        if points < 0:
            raise ValueError("[TEAM.PY] Points must be positive.")
        self.score += points
