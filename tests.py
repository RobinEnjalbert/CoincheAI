# -*- coding: utf-8 -*-

import unittest

from src.Environment.Card import Card
from src.Environment.Deck import Deck
from src.Environment.Hand import Hand
from src.Environment.Players.Player import Player
from src.Environment.Team import Team


class TestCard(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_card(self):
        """ Test correct card creation """
        card = Card(0, 0)
        self.assertEqual(card.get_value(), 0)
        self.assertEqual(card.get_color(), 0)

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
        self.assertEqual(len(deck.__cards), 32)
        self.assertEqual(deck.__cards[0].get_value(), 0)
        self.assertEqual(deck.__cards[0].get_color(), 0)
        self.assertEqual(deck.__cards[-1].get_value(), 7)
        self.assertEqual(deck.__cards[-1].get_color(), 3)

    def test_shuffle_deck(self):
        """ Test deck shuffle """
        deck = Deck()
        previous_deck = deck.__cards.copy()
        deck.shuffle()
        shuffled_deck = deck.__cards.copy()
        same, i = True, 0
        while same and i < 32:
            if previous_deck[i] != shuffled_deck[i]:
                same = False
            i += 1
        self.assertEqual(same, False)

    def test_distribute_deck(self):
        """ Test deck distribution """
        deck = Deck()
        hands = deck.distribute()
        for hand in hands:
            self.assertEqual(len(hand), 8)
        self.assertEqual(len(deck.__cards), 0)

    def test_distribute_deck_wrong_two(self):
        """ Test distribution with wrong two value """
        deck = Deck()
        self.assertRaises(ValueError, deck.distribute, 3)


class TestHand(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_hand(self):
        """ Test correct hand creation """
        deck = Deck()
        hands = deck.distribute()
        hand = Hand(hands[0])
        print(hand.hand)
        self.assertEqual(hand.hand, hands[0])
        self.assertEqual(hand.played, [1 for _ in range(8)])

    def test_create_hand_wrong_card_type(self):
        """ Test hand creation with wrong card type """
        cards = [(v_idx, c_idx) for c_idx in range(2) for v_idx in range(4)]
        self.assertRaises(TypeError, Hand, cards)

    def test_create_hand_wrong_list_type(self):
        """ Test hand creation with wrong card type """
        cards = (Card(v_idx, c_idx) for c_idx in range(2) for v_idx in range(4))
        self.assertRaises(TypeError, Hand, cards)

    def test_create_hand_wrong_list_size(self):
        """ Test hand creation with wrong card type """
        cards = [Card(v_idx, c_idx) for c_idx in range(2) for v_idx in range(3)]
        self.assertRaises(ValueError, Hand, cards)

    def test_sort_hand(self):
        """ Test correct hand sorting """
        deck = Deck()
        hands = deck.distribute()
        hand = Hand(hands[0])
        hand.sort('Spade')
        expected_hand = '[7 of Club, 8 of Club, 9 of Club, Jack of Diamond, Queen of Diamond, Queen of Spade, ' \
                        'King of Spade, Jack of Spade]'
        self.assertEqual(str(hand), expected_hand)

    def test_sort_wrong_trump(self):
        """ Test hand sorting with wrong trump value """
        deck = Deck()
        hands = deck.distribute()
        hand = Hand(hands[0])
        self.assertRaises(ValueError, hand.sort, 'trump')

    def test_play_card(self):
        """ Test correct card played """
        deck = Deck()
        hands = deck.distribute()
        hand = Hand(hands[0])
        hand.play(0)
        self.assertEqual(hand.played[0], 0)

    def test_play_card_wrong_value(self):
        deck = Deck()
        hands = deck.distribute()
        hand = Hand(hands[0])
        self.assertRaises(ValueError, hand.play, 8)


class TestPlayer(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_player(self):
        player = Player('Player1')
        self.assertEqual(player.__name, 'Player1')

    def test_create_player_wrong_name(self):
        self.assertRaises(TypeError, Player, 1)


class TestTeam(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_team(self):
        player1, player2 = Player('Player1'), Player('Player2')
        team = Team(player1, player2)
        self.assertEqual(team.players[0].__name, player1.__name)
        self.assertEqual(team.players[1].__name, player2.__name)
        self.assertEqual(team.__score, 0)

    def test_create_wrong_player_type(self):
        self.assertRaises(AssertionError, Team, 'Player1', Player('Player2'))
        self.assertRaises(AssertionError, Team, Player('Player1'), 'Player2')

    def test_add_points(self):
        team = Team(Player('Player1'), Player('Player2'))
        team.add_score(20)
        self.assertEqual(team.__score, 20)

    def test_add_points_wrong_type(self):
        team = Team(Player('Player1'), Player('Player2'))
        self.assertRaises(TypeError, team.add_score, 'zero')

    def test_add_points_wrong_value(self):
        team = Team(Player('Player1'), Player('Player2'))
        self.assertRaises(ValueError, team.add_score, -1)


if __name__ == '__main__':
    unittest.main()
