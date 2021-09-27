import pygame
from src.GUI.GUI import GUI
from src.Environment.Rules.Coinche import Coinche
from src.Environment.Players.Human import Human
from src.Environment.Players.Random import Random


if __name__ == '__main__':
    players = [Human, Random, Random, Random]
    coinche = Coinche(players)
    gui = GUI(coinche=coinche, index_player=0)
    pygame.quit()
