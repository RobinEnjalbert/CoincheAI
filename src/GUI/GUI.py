import pygame
from pygame.locals import *
from .Collection import Collection
from .constants import *


class GUI:

    def __init__(self):
        pygame.init()
        self.resolution = SCREEN_SIZE
        self.res_width, self.res_height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.display = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('CoincheAI')
        self.images = Collection()
        self.show_background()

    def show_background(self):
        self.display.blit(self.images.background, (0, 0))
        pygame.display.flip()

    def show_cards(self, hand):
        # Show cards in hand for player 0 (GUI POV)
        positions = CARD_POSITIONS[0]
        for position in positions['pair']:
            self.display.blit(self.images.back, position)
        # Show backs for other players
        for i in range(1, 4):
            positions = CARD_POSITIONS[i]
            for position in positions['pair']:
                if i == 2:
                    self.display.blit(self.images.back, position)
                else:
                    self.display.blit(pygame.transform.rotate(self.images.back, 90), position)
        pygame.display.update()

    def choose_bidding(self, bidding):
        # TODO
        pass

    def update_bidding(self, player_name, bidding):
        # TODO
        pass
