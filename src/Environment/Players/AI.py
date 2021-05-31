from .Player import Player


class AI(Player):

    def __init__(self, name, index):
        super(AI, self).__init__(name, index)
        self.__type = 'AI'

    def choose_bidding(self, bidding, previous_bidding):
        pass
