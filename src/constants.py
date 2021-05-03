# -*- coding: utf8 -*-

# Cards 
CARD_VALUES = ('7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
CARD_COLORS = ('Club', 'Diamond', 'Spade', 'Heart')
STRENGTH = {'basic': (0, 1, 2, 6, 3, 4, 5, 7),
            'asked_color': (8, 9, 10, 14, 11, 12, 13, 15),
            'trump': (16, 17, 22, 20, 23, 18, 19, 21)}

# Points
POINTS = {'standard': (0, 0, 0, 10, 2, 3, 4, 11),
          'trump': (0, 0, 14, 10, 20, 3, 4, 11),
          'belote': 20}
CONTRACTS = (80, 90, 100, 110, 120, 130, 140, 150, 160, 'capot', 'generale')
TRUMPS = ('Club', 'Diamond', 'Heart', 'Spade', 'AT', 'NT')
