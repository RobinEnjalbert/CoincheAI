from .Player import Player


class Human(Player):

    def __init__(self, name, index):
        super(Human, self).__init__(name, index)
        self.set_type('Human')

    def choose_bidding(self, bidding, previous_bidding):
        # The human player chooses on the GUI
        pass
