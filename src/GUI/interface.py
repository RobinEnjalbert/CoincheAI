import socket
import threading
import sys
import pygame
from pygame.locals import *
from skin import Skins
from locals import *


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
        skins = Skins()
        self.display.blit(skins.background, (0, 0))
        pygame.display.flip()



if __name__ == '__main__':
    gui = GUI()
    while True:
        continue

