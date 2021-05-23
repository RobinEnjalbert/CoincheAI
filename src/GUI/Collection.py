import os
import pygame
from .constants import *


class Collection:

    def __init__(self):
        img_path = os.path.realpath(os.path.dirname(__file__) + '../../../images/')
        # Background
        img = pygame.image.load(os.path.join(img_path, 'background.png'))
        self.background = pygame.transform.smoothscale(img, SCREEN_SIZE).convert()
        # Cards back
        img = pygame.image.load(os.path.join(img_path, 'back.png'))
        self.back = pygame.transform.smoothscale(img, CARD_SIZE).convert_alpha()
        # Cards front
        self.front = [[None for _ in range(8)] for _ in range(4)]
        for color in range(4):
            for value in range(8):
                filename = CARD_VALUES[value] + CARD_COLORS[color] + '.png'
                img = pygame.image.load(os.path.join(img_path, filename))
                self.front[color][value] = pygame.transform.smoothscale(img, CARD_SIZE).convert_alpha()

    def getCard(self, color, value):
        return self.front[color][value]
