import unittest

from src.Environment.Materials.Card import Card


class CardTest(unittest.TestCase):

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