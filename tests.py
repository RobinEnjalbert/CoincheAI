# -*- coding: utf-8 -*-

import unittest

from MyPackage.Card import Card
from MyPackage.Deck import Deck
from MyPackage.Player import Player
from MyPackage.Team import Team


class TestCard(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_card_correct(self):
        """ Test correct card creation """
        card = Card(0, 0)
        self.assertEqual(card.getValue(), 0)
        self.assertEqual(card.getColor(), 0)

    def test_create_card_wrong_value(self):
        """ Test card creation with wrong value """
        self.assertRaises(ValueError, Card, 8, 0)

    def test_create_card_wrong_value_type(self):
        """ Test card creation with wrong value type"""
        self.assertRaises(AssertionError, Card, 'zero', 0)

    def test_create_card_wrong_color(self):
        """ Test card creation with wrong color """
        self.assertRaises(ValueError, Card, 0, 4)

    def test_create_card_wrong_color_type(self):
        """ Test card creation with wrong color type """
        self.assertRaises(AssertionError, Card, 0, 'zero')

    def test_operator_eq(self):
        """ Test identical cards comparison """
        card1 = Card(0, 0)
        card2 = Card(0, 0)
        self.assertEqual(card1, card2)

    def test_operator_ne(self):
        """ Test not identical cards comparison """
        card1 = Card(0, 0)
        card2 = Card(0, 1)
        card3 = Card(1, 0)
        self.assertNotEqual(card1, card2)
        self.assertNotEqual(card1, card3)
        self.assertNotEqual(card2, card3)


class TestDeck(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_deck(self):
        """ Test deck creation """
        deck = Deck()
        self.assertEqual(len(deck.cardList), 32)
        self.assertEqual(deck.cardList[0].getValue(), 0)
        self.assertEqual(deck.cardList[0].getColor(), 0)
        self.assertEqual(deck.cardList[-1].getValue(), 7)
        self.assertEqual(deck.cardList[-1].getColor(), 3)

    def test_shuffle_deck(self):
        """ Test deck shuffle """
        deck = Deck()
        deck.shuffle()
        test = False
        for i in range(7):
            if deck.cardList[i].getColor() != 0:
                test = True
        self.assertEqual(test, True)

    def test_distribute_deck(self):
        """ Test deck distribution """
        deck = Deck()
        hands = deck.distribute(two=1)
        for hand in hands:
            self.assertEqual(len(hand), 8)
        self.assertEqual(len(deck.cardList), 0)

    def test_distribute_deck_wrong_two(self):
        """ Test test distribution with wrong two value """
        deck = Deck()
        self.assertRaises(ValueError, deck.distribute, 3)


class TestPlayer(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_player(self):
        player = Player('Player1')
        self.assertEqual(player.name, 'Player1')

    def test_create_player_wrong_name(self):
        self.assertRaises(TypeError, Player, 1)


class TestTeam(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_team(self):
        player1, player2 = Player('Player1'), Player('Player2')
        team = Team(player1, player2)
        self.assertEqual(team.players[0].name, player1.name)
        self.assertEqual(team.players[1].name, player2.name)
        self.assertEqual(team.score, 0)

    def test_create_wrong_player_type(self):
        self.assertRaises(AssertionError, Team, 'Player1', Player('Player2'))
        self.assertRaises(AssertionError, Team, Player('Player1'), 'Player2')

    def test_add_points(self):
        team = Team(Player('Player1'), Player('Player2'))
        team.addPoints(20)
        self.assertEqual(team.score, 20)

    def test_add_points_wrong_type(self):
        team = Team(Player('Player1'), Player('Player2'))
        self.assertRaises(TypeError, team.addPoints, 'zero')

    def test_add_points_wrong_value(self):
        team = Team(Player('Player1'), Player('Player2'))
        self.assertRaises(ValueError, team.addPoints, -1)


if __name__ == '__main__':
    unittest.main()
