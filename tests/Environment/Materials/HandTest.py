import unittest

from src.Environment.Materials.Card import Card
from src.Environment.Materials.Deck import Deck
from src.Environment.Materials.Hand import Hand


class HandTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_hand(self):
        """ Test correct hand creation """
        deck = Deck()
        hands = deck.distribute()
        hand = Hand()
        hand.set(hands[0])
        self.assertEqual(hand.get(full=True), hands[0])
        self.assertEqual(hand.get(full=False), hands[0])

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
        hand = Hand()
        self.assertRaises(ValueError, hand.set, cards)

    def test_sort_hand(self):
        """ Test correct hand sorting """
        deck = Deck()
        hands = deck.distribute()
        hand = Hand()
        hand.set(hands[0])
        hand.sort(3)
        expected_hand = '[7 of Club, 8 of Club, 9 of Club, Jack of Diamond, Queen of Diamond, Queen of Spade, ' \
                        'King of Spade, Jack of Spade]'
        self.assertEqual(str(hand), expected_hand)

    def test_sort_wrong_trump(self):
        """ Test hand sorting with wrong trump value """
        deck = Deck()
        hands = deck.distribute()
        hand = Hand()
        hand.set(hands[0])
        self.assertRaises(ValueError, hand.sort, 'trump')

    def test_play_card(self):
        """ Test correct card played """
        deck = Deck()
        hands = deck.distribute()
        hand = Hand()
        hand.set(hands[0])
        hand.play(0)
        self.assertEqual(len(hand.get()), 7)

    def test_play_card_wrong_value(self):
        deck = Deck()
        hands = deck.distribute()
        hand = Hand()
        hand.set(hands[0])
        self.assertRaises(ValueError, hand.play, 8)




