from constants import CONTRACTS, TRUMPS


class Bidding:

    def __init__(self, players, teams, start_player):
        self.players = players
        self.teams = teams
        self.teams_id = {'Player0': 0, 'Player1': 1,
                         'Player2': 0, 'Player3': 1}
        self.start_player = start_player
        self.start_team = self.teams_id[players[start_player].name]
        self.bidding = {'contracts': None, 'trump': None}
        self.bidding_history = []

    def play(self):
        bidding_team = None
        player_turn = self.start_player
        passed = 0
        while passed != 4:
            contract, trump = self.players[player_turn].choose_bidding(self.bidding_history)
            bidding = {'contracts': contract, 'trump': trump}
            self.bidding_history.append(bidding)
            if contract != 'pass':
                self.bidding = bidding
                bidding_team = self.teams_id[self.players[player_turn].name]
                passed = 4 if contract == 'generale' else 1
            else:
                passed += 1
            player_turn = (player_turn + 1) % 4
        return self.bidding, bidding_team
