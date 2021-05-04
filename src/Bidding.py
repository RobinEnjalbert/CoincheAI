from constants import CONTRACTS, TRUMPS


class Bidding:

    def __init__(self, players, teams, start_player):
        self.players = players
        self.teams = teams
        self.teams_id = {'Player0': 0, 'Player1': 1,
                         'Player2': 0, 'Player3': 1}
        self.start_player = start_player
        self.contract = None
        self.contract_history = None
        self.available_contracts = CONTRACTS

    def play_bidding(self):
        bettor = None
        player_turn = self.start_player
        passed = 0
        while passed != 4:
            bidding = self.players[player_turn].choose_bidding(self.contract_history)
            if bidding is not None:
                self.contract = bidding
                bettor = self.teams_id[self.players[player_turn].name]
                if bidding.value == 'generale':
                    passed = 4
                else:
                    passed = 1
            else:
                passed += 1
        # TODO: find a way to store previous contracts to give to player
        return self.contract, bettor
