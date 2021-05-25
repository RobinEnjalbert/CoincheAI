# GUI
FPS = 30

# Screen size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Cards size
CARD_WIDTH = SCREEN_WIDTH // 12
CARD_HEIGHT = SCREEN_WIDTH // 8
CARD_SIZE = (CARD_WIDTH, CARD_HEIGHT)
# Cards values
CARD_VALUES = ('7', '8', '9', '10', 'J', 'Q', 'K', 'A')
CARD_COLORS = ('C', 'D', 'S', 'H')
# Cards positions
margin = CARD_HEIGHT // 3
x_min = -margin
x_max = SCREEN_WIDTH - CARD_HEIGHT + margin
y_min = -margin
y_max = SCREEN_HEIGHT - CARD_HEIGHT + margin
CARD_POSITIONS = {0: {'pair': (((i+7.75)*CARD_WIDTH//2, y_max) for i in range(8)),
                      'impair': (((i+8.25)*CARD_WIDTH//2, y_max) for i in range(7))},
                  1: {'pair': ((x_min, (i+2.25)*CARD_WIDTH//2) for i in range(8)),
                      'impair': ((x_min, (i+2.75)*CARD_WIDTH//2) for i in range(8))},
                  2: {'pair': (((i+7.75)*CARD_WIDTH//2, y_min) for i in range(8)),
                      'impair': (((i+8.25)*CARD_WIDTH//2, y_min) for i in range(7))},
                  3: {'pair': ((x_max, (i+2.25)*CARD_WIDTH//2) for i in range(8)),
                      'impair': ((x_max, (i+2.75)*CARD_WIDTH//2) for i in range(8))}}
PLAYER_CLICK = {'pair': {},
                'impair': {}}

# Colors
WHITE = (255, 255, 255)
LIGHTGREY = (191, 191, 191)
GREY = (127, 127, 127)
DARKGREY = (63, 63, 63)
BLACK = (0, 0, 0)

# Bidding
CONTRACTS = ('pass', '80', '90', '100', '110', '120', '130', '140', '150', '160', 'Capot', 'Generale')
TRUMPS = ('Club', 'Diamond', 'Heart', 'Spade', 'AT', 'NT')
# Bidding window: positions, width, height
BID_POSITION = (SCREEN_WIDTH * 1 / 3, SCREEN_HEIGHT * 1 / 3)
BID_SIZE = (SCREEN_WIDTH * 1 / 3, SCREEN_HEIGHT * 1 / 3)
# Bidding contracts
CONT_WIDTH, CONT_HEIGHT = BID_SIZE[0] * 1 / 8, BID_SIZE[1] * 1 / 6
CONT_X_MARGIN, CONT_Y_MARGIN = CONT_WIDTH * 2 / 7, CONT_HEIGHT * 1 / 3
CONTRACT_BOX = (BID_POSITION[0], BID_POSITION[1], BID_SIZE[0], BID_SIZE[1] / 2)
CONT_POSITION = ((BID_POSITION[0] + 1*CONT_X_MARGIN + 0*CONT_WIDTH, BID_POSITION[1] + 1*CONT_Y_MARGIN + 0*CONT_HEIGHT),
                 (BID_POSITION[0] + 2*CONT_X_MARGIN + 1*CONT_WIDTH, BID_POSITION[1] + 1*CONT_Y_MARGIN + 0*CONT_HEIGHT),
                 (BID_POSITION[0] + 3*CONT_X_MARGIN + 2*CONT_WIDTH, BID_POSITION[1] + 1*CONT_Y_MARGIN + 0*CONT_HEIGHT),
                 (BID_POSITION[0] + 4*CONT_X_MARGIN + 3*CONT_WIDTH, BID_POSITION[1] + 1*CONT_Y_MARGIN + 0*CONT_HEIGHT),
                 (BID_POSITION[0] + 5*CONT_X_MARGIN + 4*CONT_WIDTH, BID_POSITION[1] + 1*CONT_Y_MARGIN + 0*CONT_HEIGHT),
                 (BID_POSITION[0] + 6*CONT_X_MARGIN + 5*CONT_WIDTH, BID_POSITION[1] + 1*CONT_Y_MARGIN + 0*CONT_HEIGHT),
                 (BID_POSITION[0] + 1*CONT_X_MARGIN + 0*CONT_WIDTH, BID_POSITION[1] + 2*CONT_Y_MARGIN + 1*CONT_HEIGHT),
                 (BID_POSITION[0] + 2*CONT_X_MARGIN + 1*CONT_WIDTH, BID_POSITION[1] + 2*CONT_Y_MARGIN + 1*CONT_HEIGHT),
                 (BID_POSITION[0] + 3*CONT_X_MARGIN + 2*CONT_WIDTH, BID_POSITION[1] + 2*CONT_Y_MARGIN + 1*CONT_HEIGHT),
                 (BID_POSITION[0] + 4*CONT_X_MARGIN + 3*CONT_WIDTH, BID_POSITION[1] + 2*CONT_Y_MARGIN + 1*CONT_HEIGHT),
                 (BID_POSITION[0] + 6*CONT_X_MARGIN + 4*CONT_WIDTH, BID_POSITION[1] + 2*CONT_Y_MARGIN + 1*CONT_HEIGHT))
CONT_SIZE = ((CONT_WIDTH, CONT_HEIGHT),
             (CONT_WIDTH, CONT_HEIGHT),
             (CONT_WIDTH, CONT_HEIGHT),
             (CONT_WIDTH, CONT_HEIGHT),
             (CONT_WIDTH, CONT_HEIGHT),
             (CONT_WIDTH, CONT_HEIGHT),
             (CONT_WIDTH, CONT_HEIGHT),
             (CONT_WIDTH, CONT_HEIGHT),
             (CONT_WIDTH, CONT_HEIGHT),
             (CONT_WIDTH + CONT_X_MARGIN, CONT_HEIGHT),
             (2*CONT_WIDTH, CONT_HEIGHT))
