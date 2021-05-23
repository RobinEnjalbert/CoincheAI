import pygame
from pygame.locals import *
from src.GUI.GUI import GUI
from src.Environment.Coinche import Coinche


if __name__ == '__main__':
    gui = GUI()
    coinche = Coinche()
    gui.show_cards(None)
    continue_jeu = True
    while continue_jeu:
        for event in pygame.event.get():
            if event.type == QUIT:
                continue_jeu = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(event.pos)
    pygame.quit()
