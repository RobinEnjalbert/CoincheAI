import unittest

from src.Environment.Materials.Deck import Deck


class DeckTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_deck(self):
        """ Test deck creation """
        deck = Deck()
        self.assertEqual(len(deck), 32)
        self.assertEqual(deck.get()[0].get_value(), 0)
        self.assertEqual(deck.get()[0].get_color(), 0)
        self.assertEqual(deck.get()[-1].get_value(), 7)
        self.assertEqual(deck.get()[-1].get_color(), 3)

    def test_shuffle_deck(self):
        """ Test deck shuffle """
        deck = Deck()
        previous_deck = deck.get()
        deck.shuffle()
        shuffled_deck = deck.get()
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
        self.assertEqual(len(deck), 0)

    def test_distribute_deck_wrong_two(self):
        """ Test distribution with wrong two value """
        deck = Deck()
        self.assertRaises(ValueError, deck.distribute, 3)

