# -*- coding: utf8 -*-

from src.Environment.constants import CONTRACTS, TRUMPS


class Bidding:

    def __init__(self, players, teams, first_player, gui):
        self.players = players
        self.teams = teams
        self.teams_id = {teams[0].players[0].get_name(): 0, teams[1].players[0].get_name(): 1,
                         teams[0].players[1].get_name(): 0, teams[1].players[1].get_name(): 1}
        self.first_player = first_player
        self.bidding = [None, None]
        self.previous_bidding = []
        self.gui = gui

    def play_bidding(self):
        # TODO: add coinche variable as output
        bidding_team = None
        player_turn = self.first_player
        passed = 0
        while passed != 4:
            # Ask the actual player to bid
            actual_player = self.players[player_turn]
            if actual_player.get_type() == 'Human':
                contract, trump = self.gui.choose_bidding(self.bidding)
            else:
                contract, trump = actual_player.choose_bidding(self.bidding, self.previous_bidding)
            # Check the bidding value
            if contract not in range(12):
                raise ValueError("[BIDDING.PY] The contract index must be in [0:11].")
            if trump not in range(6):
                raise ValueError("[BIDDING.PY] The trump index must be in [0:5].")
            # Update bidding and passed counter
            self.gui.update_bidding(player_turn, [contract, trump])
            self.previous_bidding.append([contract, trump])
            if contract != 0:   # The player doesn't pass
                self.bidding = [contract, trump]
                bidding_team = self.teams_id[actual_player.get_name()]
                passed = 4 if contract == len(CONTRACTS) - 1 else 1     # All the other should pass if "generale"
            else:
                passed += 1
            # Next player to bid
            player_turn = (player_turn + 1) % 4
        return self.bidding, bidding_team

    def __str__(self):
        if self.bidding[0] is None:
            return 'None'
        else:
            return "{} {}".format(CONTRACTS[self.bidding[0]], TRUMPS[self.bidding[1]])

    def __repr__(self):
        return str(self)
