import pygame
from pygame.locals import *

from Collection import Collection
from constants import *


class InterfaceError(Exception):

    def __init__(self, cause, details=""):
        self.cause = cause
        self.details = details

    def __repr__(self):
        return self.cause + self.details


class GUI:

    def __init__(self):
        pygame.init()
        self.resolution = SCREEN_RES
        self.res_width, self.res_height = RES_WIDTH, RES_HEIGHT
        self.display = pygame.display.set_mode(SCREEN_RES)
        pygame.display.set_caption('CoincheAI')
        self.images = Collection()
        self.show_background()

    def show_background(self):
        self.display.blit(self.images.background, (0, 0))
        pygame.display.flip()

    def show_cards(self, hand):
        # show cards for hand with indice player 0 (GUI POV)
        # show backs for players 1?2?3
        for i in range(4):
            positions = CARD_POSITIONS[i]
            for position in positions['pair']:
                self.display.blit(self.images.back, position)
        self.display.blit(self.images.getCard(1,1), (10, 10))
        pygame.display.update()



if __name__ == '__main__':
    gui = GUI()
    gui.show_cards(None)
    while True:
        continue

