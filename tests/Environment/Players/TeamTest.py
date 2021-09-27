import unittest

from src.Environment.Players.Team import Team
from src.Environment.Players.Player import Player


class TeamTest(unittest.TestCase):

    def setUp(self):
        self.team = Team(Player('Player1', 1), Player('Player2', 2))

    def test_create_team(self):
        player1, player2 = Player('Player1', 1), Player('Player2', 2)
        team = Team(player1, player2)
        self.assertEqual(team.players[0].get_name(), player1.get_name())
        self.assertEqual(team.players[1].get_name(), player2.get_name())
        self.assertEqual(team.get_score(), 0)

    def test_create_wrong_player_type(self):
        self.assertRaises(AssertionError, Team, 'Player1', Player('Player2', 2))
        self.assertRaises(AssertionError, Team, Player('Player1', 1), 'Player2')

    def test_add_points(self):
        self.team.add_score(20)
        self.assertEqual(self.team.get_score(), 20)

    def test_add_points_wrong_type(self):
        self.assertRaises(TypeError, self.team.add_score, 'zero')

    def test_add_points_wrong_value(self):
        self.assertRaises(ValueError, self.team.add_score, -1)

