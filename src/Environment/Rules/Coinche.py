# -*- coding: utf8 -*-

from src.Environment.Players.Team import Team
from src.Environment.Materials.Deck import Deck
from src.Environment.Rules.Bidding import Bidding

import random


class Coinche:

    def __init__(self, players):
        player_names = ['Player0', 'Player1', 'Player2', 'Player3']
        self.players = [players[i](name=player_names[i], index=i) for i in range(4)]
        self.teams = [Team(self.players[0], self.players[2]), Team(self.players[1], self.players[3])]
        self.first_player = 0
        self.deck = Deck()
        self.gui = None

    def play_game(self, gui):
        self.gui = gui
        self.deck.shuffle()
        while self.teams[0].get_score() < 1000 and self.teams[1].get_score() < 1000 and not self.gui.quitGUI:
            self.distribute_cards()
            bidding_phase = Bidding(self.players, self.teams, self.first_player, self.gui)
            bidding, bidding_team = bidding_phase.play_bidding()
            if bidding_team is None:
                self.collect_players_cards()
            else:
                # TODO: Round
                # TODO: Scores
                # self.collect_teams_cards(bidding_team)
                self.collect_players_cards()
                self.teams[0].won_cards, self.teams[1].won_cards = [], []
            self.first_player = (self.first_player + 1) % 4

    def distribute_cards(self):
        self.deck.cut()
        hands = self.deck.distribute(random.randint(0, 2))
        for i in range(4):
            idx_player = (self.first_player + i) % 4
            self.players[idx_player].hand.set(hands[i])
            self.players[idx_player].hand.sort()
            self.gui.show_cards(idx_player)

    def sort_all_hands(self, trump):
        for player in self.players:
            player.hand.sort(trump)

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
