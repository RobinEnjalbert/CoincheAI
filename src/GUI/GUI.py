import pygame
from pygame.locals import *
from .Collection import Collection
from .constants import *


class GUI:

    def __init__(self, coinche, index_player):
        pygame.init()
        self.quitGUI = False
        # Display
        self.resolution = SCREEN_SIZE
        self.res_width, self.res_height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.display = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('CoincheAI')
        # Images, font
        self.images = Collection()
        self.font = pygame.font.SysFont("Arial", 30)
        self.show_background()
        # Coinche
        self.coinche = coinche
        self.contract_clicked = False
        self.trump_clicked = False
        self.index_players = [(index_player + i) % 4 for i in range(4)]
        # Auto start
        self.mainLoop()

    def mainLoop(self):
        self.coinche.play_game(self)

    def show_background(self):
        self.display.blit(self.images.background, (0, 0))
        pygame.display.flip()
        self.show_players_log()

    def show_players_log(self, actual_player=None, contract=None):
        print(actual_player, contract)
        for i in range(4):
            if actual_player is None or i == actual_player:
                rect = pygame.draw.rect(self.display, WHITE, PLAYER_LOG_POSITIONS[i] + PLAYER_LOG_SIZE)
                # Player name
                text = self.font.render(f"Player {i+1}", True, BLACK)
                x_t, y_t = (rect.width - text.get_width()) / 2, (0.5*rect.height - text.get_height()) / 2
                self.display.blit(text, (PLAYER_LOG_POSITIONS[i][0] + x_t, PLAYER_LOG_POSITIONS[i][1] + y_t))
                # Player bidding
                text_str = '-' if actual_player is None else CONTRACTS[contract[0]] + ' ' + TRUMPS[contract[1]]
                text = self.font.render(text_str, True, BLACK)
                x_t = (rect.width - text.get_width()) / 2
                y_t = 0.5 * rect.height + (0.5 * rect.height - text.get_height()) / 2
                self.display.blit(text, (PLAYER_LOG_POSITIONS[i][0] + x_t, PLAYER_LOG_POSITIONS[i][1] + y_t))

    def show_cards(self, player):
        # Count the number of cards in hand
        hand = self.coinche.players[player].hand.get()
        parity = 'pair' if len(hand) % 2 == 0 else 'impair'
        max_parity = 8 if parity == 'pair' else 7
        # Get the positions of the cards
        positions = CARD_POSITIONS[self.index_players[player]][parity]
        idx_positions = range((max_parity - len(hand)) // 2, (max_parity + len(hand)) // 2)
        # Show cards in hand for player 0
        if self.index_players[player] == 0:
            for i in range(len(hand)):
                card = hand[i]
                self.display.blit(self.images.get_card(card.get_color(), card.get_value()), positions[idx_positions[i]])
        # Show backs without rotation for player 2
        elif self.index_players[player] == 2:
            for idx in idx_positions:
                self.display.blit(self.images.back, positions[idx])
        # Show backs with rotation for side players
        else:
            for idx in idx_positions:
                self.display.blit(pygame.transform.rotate(self.images.back, 90), positions[idx])
        pygame.display.update()

    def choose_bidding(self, bidding):
        prev_contract, trump = bidding[0], bidding[1]
        contract = prev_contract
        # 1) Display the values and trumps
        contract_buttons, trump_buttons, validate_buttons = self.show_bidding_window(prev_contract)
        contract_box = pygame.Rect(CONTRACT_BOX)
        trump_box = pygame.Rect(TRUMP_BOX)
        validate_box = pygame.Rect(VAL_BOX)
        # 2) While no choice, wait for player validation
        validation = False
        while not validation:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    pointer = event.pos
                    # Click on contract
                    if contract_box.collidepoint(pointer):
                        contract = self.click_contract(pointer, contract_buttons, prev_contract, contract)
                    # Click on trump
                    elif trump_box.collidepoint(pointer):
                        trump = self.click_trump(pointer, trump_buttons, trump)
                    # Click on validation button
                    elif validate_box.collidepoint(pointer):
                        val = self.click_validate(pointer, validate_buttons)
                        if val is not None:
                            validation = True
                            if val == 0:
                                contract, trump = 0, 5
        return contract + 1, trump

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
        validate_buttons = []
        for i in range(3):
            b = pygame.draw.rect(self.display, LIGHTGREY, VAL_POSITION[i] + VAL_SIZE[i])
            self.set_validate_text(b, i)
            validate_buttons.append(b)
        # Render
        pygame.display.update()
        return contracts_buttons, trump_buttons, validate_buttons

    def set_contract_text(self, button, idx):
        text = self.font.render(CONTRACTS[idx + 1], True, BLACK)
        x_t, y_t = self.center_text(button, text)
        self.display.blit(text, (CONT_POSITION[idx][0] + x_t, CONT_POSITION[idx][1] + y_t))

    def set_trump_text(self, button, idx):
        text = self.font.render(TRUMPS[idx], True, BLACK)
        x_t, y_t = self.center_text(button, text)
        self.display.blit(text, (TRUMP_POSITION[idx][0] + x_t, TRUMP_POSITION[idx][1] + y_t))

    def set_validate_text(self, button, idx):
        text = self.font.render(VAL[idx], True, BLACK)
        x_t, y_t = self.center_text(button, text)
        self.display.blit(text, (VAL_POSITION[idx][0] + x_t, VAL_POSITION[idx][1] + y_t))

    def center_text(self, button, text):
        return (button.width - text.get_width()) / 2, (button.height - text.get_height()) / 2

    def click_contract(self, pointer, buttons, prev_contract, contract):
        for i in range(len(buttons)):
            b = buttons[i]
            if b.collidepoint(pointer) and i != contract:
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
            if b.collidepoint(pointer) and i != trump:
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

    def click_validate(self, pointer, buttons):
        validation = None
        if buttons[0].collidepoint(pointer):
            validation = 0
        elif buttons[1].collidepoint(pointer) and self.contract_clicked and self.trump_clicked:
            validation = 1
        elif buttons[2].collidepoint(pointer):
            validation = 2
        return validation

    def update_bidding(self, actual_player, contract):
        self.coinche.sort_all_hands(contract[1])
        self.show_cards(self.index_players.index(0))
        # Show the contract aside the actual player
        self.show_players_log(actual_player, contract)
        # TODO: handle special cases
