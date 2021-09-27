import unittest

from src.Environment.Players.Player import Player


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player('Player1', 1)

    def test_create_player(self):
        self.assertEqual(self.player.get_name(), 'Player1')
        self.assertEqual(self.player.get_index(), 1)

    def test_create_player_wrong_name(self):
        self.assertRaises(TypeError, Player, (1, 'Player1'))

    def test_create_player_wrong_index(self):
        self.assertRaises(TypeError, Player, ('Player1', 'Player1'))

    def test_create_player_wrong_type(self):
        self.assertRaises(ValueError, self.player.set_type, 'Player')
