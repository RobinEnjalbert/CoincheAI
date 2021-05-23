import random
from .Player import Player


class Random(Player):

    def __init__(self, name):
        super(Random, self).__init__(name)
        self.__type = 'Random'

    def choose_bidding(self, bidding, previous_bidding):
        min_contract = bidding[0] + 1 if bidding[0] is not None else 0
        contract = random.randint(min_contract, 11)
        trump = random.randint(0, 5)
        return contract, trump
