from Player import Player
from Team import Team
from Deck import Deck
from Bidding import Bidding
from Round import Round

import random


class Coinche:

    def __init__(self):
        player_names = ['Player0', 'Player1', 'Player2', 'Player3']
        self.players = [Player(name=name) for name in player_names]
        self.teams = [Team(self.players[0], self.players[2]), Team(self.players[1], self.players[2])]
        self.start_player = 0
        self.deck = Deck()
        self.scores = [0, 0]

    def play_game(self):
        self.deck.shuffle()
        while self.scores[0] < 1000 and self.scores[1] < 1000:
            self.distributeCards()
            bidding = Bidding(self.players, self.teams, self.start_player)
            contract, bettor = bidding.play_bidding()
            if contract is None:
                self.pickupPlayersCards()
            else:
                # TODO: Round
                # TODO :Update scores
                self.pickupTeamsCards(self.teams[0].won_cards, self.teams[1].won_cards, bettor)
                self.teams[0].won_cards, self.teams[1].won_cards = [], []
            self.start_player = (self.start_player + 1) % 4

    def distributeCards(self):
        self.deck.cut()
        hands = self.deck.distribute(random.randint(0, 2))
        for i in range(4):
            idx_player = (self.start_player + i) % 4
            self.players[idx_player].hand = hands[i]

    def pickupPlayersCards(self):
        deck = []
        for i in range(4):
            idx_player = (self.start_player + i) % 4
            deck += self.players[idx_player].hand
            self.players[idx_player].hand = []
        self.deck.cardList = deck

    def pickupTeamsCards(self, deck1, deck2, bettor):
        deck = deck1 + deck2 if bettor == 0 else deck2 + deck1
        self.deck.cardList = deck


coinche = Coinche()
coinche.distributeCards()
for player in coinche.players:
    print(player)
