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
        self.contract_clicked = False
        self.trump_clicked = False

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
        prev_contract, trump = bidding[0], bidding[1]
        contract = prev_contract
        # 1) Display the values and trumps
        contract_buttons, trump_buttons = self.show_bidding_window(prev_contract)
        contract_box = pygame.Rect(CONTRACT_BOX)
        trump_box = pygame.Rect(TRUMP_BOX)
        # 2) While no choice, wait for player validation
        validation = False
        while not validation:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    pointer = event.pos
                    # Click on contract
                    if contract_box.collidepoint(pointer):
                        contract = self.click_contract(pointer, contract_buttons, prev_contract, contract)
                        if contract is not None:
                            print(CONTRACTS[contract + 1])
                    # Click on trump
                    elif trump_box.collidepoint(pointer):
                        trump = self.click_trump(pointer, trump_buttons, trump)
                        if trump is not None:
                            print(TRUMPS[trump])
                    # Click on validation button
                    # Todo
        return contract, trump

    def show_bidding_window(self, contract):
        # Draw window
        pygame.draw.rect(self.display, WHITE, WIN_POSITION + WIN_SIZE)
        # Draw contracts
        contracts_buttons = []
        for i in range(11):
            color = LIGHTGREY if contract is None or i > contract else DARKGREY
            b = pygame.draw.rect(self.display, color, CONT_POSITION[i] + CONT_SIZE[i])
            self.set_contract_text(b, i)
            contracts_buttons.append(b)
        self.contract_clicked = False
        # Draw trumps
        trump_buttons = []
        for i in range(6):
            b = pygame.draw.rect(self.display, LIGHTGREY, TRUMP_POSITION[i] + TRUMP_SIZE[i])
            self.set_trump_text(b, i)
            trump_buttons.append(b)
        self.trump_clicked = False
        # Draw Coinche, Validate, Pass
        # Todo
        # Render
        pygame.display.update()
        return contracts_buttons, trump_buttons

    def set_contract_text(self, button, idx):
        # Center the text in the button
        text = self.font.render(CONTRACTS[idx + 1], True, BLACK)
        x_t, y_t = self.center_text(button, text)
        self.display.blit(text, (CONT_POSITION[idx][0] + x_t, CONT_POSITION[idx][1] + y_t))

    def set_trump_text(self, button, idx):
        text = self.font.render(TRUMPS[idx], True, BLACK)
        x_t, y_t = self.center_text(button, text)
        self.display.blit(text, (TRUMP_POSITION[idx][0] + x_t, TRUMP_POSITION[idx][1] + y_t))

    def center_text(self, button, text):
        return (button.width - text.get_width()) / 2, (button.height - text.get_height()) / 2

    def click_contract(self, pointer, buttons, prev_contract, contract):
        for i in range(len(buttons)):
            b = buttons[i]
            if b.collidepoint(pointer):
                if prev_contract is None or i > prev_contract:
                    pygame.draw.rect(self.display, GREY, CONT_POSITION[i] + CONT_SIZE[i])
                    self.set_contract_text(buttons[i], i)
                    if self.contract_clicked:
                        pygame.draw.rect(self.display, LIGHTGREY, CONT_POSITION[contract] + CONT_SIZE[contract])
                        self.set_contract_text(buttons[contract], contract)
                    self.contract_clicked = True
                    contract = i
                    pygame.display.update()
                break
        return contract

    def click_trump(self, pointer, buttons, trump):
        for i in range(len(buttons)):
            b = buttons[i]
            if b.collidepoint(pointer):
                pygame.draw.rect(self.display, GREY, TRUMP_POSITION[i] + TRUMP_SIZE[i])
                self.set_trump_text(buttons[i], i)
                if self.trump_clicked:
                    pygame.draw.rect(self.display, LIGHTGREY, TRUMP_POSITION[trump] + TRUMP_SIZE[trump])
                    self.set_trump_text(buttons[trump], trump)
                self.trump_clicked = True
                trump = i
                pygame.display.update()
                break
        return trump
