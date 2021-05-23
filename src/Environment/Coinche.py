# -*- coding: utf8 -*-

from src.Environment.Players.Player import Player
from Team import Team
from Deck import Deck
from Bidding import Bidding

import random


class Coinche:

    def __init__(self, gui=None):
        self.gui = gui
        player_names = ['Player0', 'Player1', 'Player2', 'Player3']
        self.players = [Player(name=name) for name in player_names]
        self.teams = [Team(self.players[0], self.players[2]), Team(self.players[1], self.players[2])]
        self.first_player = 0
        self.deck = Deck()

    def play_game(self):
        self.deck.shuffle()
        while self.teams[0].get_score() < 1000 and self.teams[1].get_score() < 1000:
            self.distribute_cards()
            bidding_phase = Bidding(self.players, self.teams, self.first_player, self.gui)
            bidding, bidding_team = bidding_phase.play_bidding()
            if bidding_team is None:
                self.collect_players_cards()
            else:
                # TODO: Round
                # TODO: Scores
                self.collect_teams_cards(bidding_team)
                self.teams[0].won_cards, self.teams[1].won_cards = [], []
            self.first_player = (self.first_player + 1) % 4

    def distribute_cards(self):
        self.deck.cut()
        hands = self.deck.distribute(random.randint(0, 2))
        for i in range(4):
            idx_player = (self.first_player + i) % 4
            self.players[idx_player].hand.set(hands[i])

    def collect_players_cards(self):
        deck = []
        for i in range(4):
            idx_player = (self.first_player + i) % 4
            deck += self.players[idx_player].hand.get(full=True)
        self.deck.reset(deck)

    def collect_teams_cards(self, bidding_team):
        deck0, deck1 = self.teams[0].won_cards, self.teams[1].won_cards
        deck = deck0 + deck1 if bidding_team == 0 else deck1 + deck0
        self.deck.reset(deck)


coinche = Coinche()
coinche.distribute_cards()
for player in coinche.players:
    print(player)
