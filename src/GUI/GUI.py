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
        self.font = pygame.font.SysFont("Arial", 30)
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
        contract, color = bidding[0], bidding[1]
        # 1) Display the values and trumps
        contract_buttons = self.show_bidding(contract)
        # 2) While no choice, wait for player validation
        validation = False
        """while not validation:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    pointer = event.pos  # (x, y) location of pointer
                    for i in range(len(contract_buttons)):
                        b = contract_buttons[i]
                        if b.collidepoint(pointer):
                            print(CONTRACTS[i+1])
                            break"""

    def show_bidding(self, contract):
        # Draw window
        pygame.draw.rect(self.display, WHITE, BID_POSITION + BID_SIZE)
        # Draw contracts
        contracts_buttons = []
        for i in range(11):
            b = pygame.draw.rect(self.display, LIGHTGREY, CONT_POSITION[i] + CONT_SIZE[i])
            self.set_contract_text(b, i)
            contracts_buttons.append(b)
        # Render
        pygame.display.update()
        return contracts_buttons

    def set_contract_text(self, button, idx):
        # Center the text in the button
        text = self.font.render(CONTRACTS[idx + 1], True, BLACK)
        x_t, y_t = (button.width - text.get_width()) / 2, (button.height - text.get_height()) / 2
        self.display.blit(text, (CONT_POSITION[idx][0] + x_t, CONT_POSITION[idx][1] + y_t))

    def update_bidding(self, player_name, bidding):
        # TODO
        pass
