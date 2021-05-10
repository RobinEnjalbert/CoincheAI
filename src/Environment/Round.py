# -*- coding: utf8 -*-

from constants import *

class Round:
    """
    Round class: A round is composed of 8 turns.
    Attributes:
        trump = idx, defines the trumps for the round in TRUMPS[idx]
        contract = idx, defines the contract values for the round in CONTRACTS[idx]
        belote = {bool, bool} to track if "belote" and "rebelote" were called
        trick = actual trick
        player1 = first player / master player
    """
    def __init__(self, trump, contract, players, attack_team):
        if trump not in range(6):
            raise ValueError("[ROUND.PY] Unknown value {} for trump.".format(trump))
        if contract not in CARD_VALUES:
            raise ValueError("[ROUND.PY] Unknown value {} for contract.".format(contract))
        self.trump = trump
        self.contract = contract
        self.players = players
        self.attackTeam = attack_team
        self.player1 = players[0]
        self.belote = [False, False]

    def round(self):
        attack_tricks = []
        defense_tricks = []
        for trick in range(8):
            cards = self.trick()
            self.defineFirstPlayer()
            if self.players[self.player1] in self.attackTeam:
                attack_tricks.append(*cards)
            else:
                defense_tricks.append(*cards)
        count = self.countPoints(attack_tricks, defense_tricks)
        return count, attack_tricks + defense_tricks

    def trick(self):
        for i in range(4):
            j = (i + self.player1) % 4
            # TODO
        return []

    def defineFirstPlayer(self):
        pass

    def countPoints(self, attack_tricks, defense_tricks):
        points = [0, 0]
        for card in attack_tricks:
            if card.color == self.trump:
                points[0] += POINTS['atout'][card.value]
            else:
                points[0] += POINTS['standard'][card.value]
        for card in defense_tricks:
            if card.color == self.trump:
                points[1] += POINTS['atout'][card.value]
            else:
                points[1] += POINTS['standard'][card.value]
        pass
