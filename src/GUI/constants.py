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
x0 = [(SCREEN_WIDTH - 4.5*CARD_WIDTH)//2, ((SCREEN_WIDTH - 4*CARD_WIDTH)//2)]
x2 = [(SCREEN_WIDTH - 2.75*CARD_WIDTH)//2, ((SCREEN_WIDTH - 2.5*CARD_WIDTH)//2)]
y1 = [(SCREEN_HEIGHT - 2.75*CARD_WIDTH)//2, (SCREEN_HEIGHT - 2.5*CARD_WIDTH)//2]
CARD_POSITIONS = {0: {'pair':   [(x0[0]+i*CARD_WIDTH//2, y_max) for i in range(8)],
                      'impair': [(x0[1]+i*CARD_WIDTH//2, y_max) for i in range(7)]},
                  1: {'pair':   [(x_min, y1[0]+i*CARD_WIDTH//4) for i in range(8)],
                      'impair': [(x_min, y1[1]+i*CARD_WIDTH//4) for i in range(8)]},
                  2: {'pair':   [(x2[0]+i*CARD_WIDTH//4, y_min) for i in range(8)],
                      'impair': [(x2[1]+i*CARD_WIDTH//4, y_min) for i in range(7)]},
                  3: {'pair':   [(x_max, y1[0]+i*CARD_WIDTH//4) for i in range(8)],
                      'impair': [(x_max, y1[1]+i*CARD_WIDTH//4) for i in range(8)]}}
PLAYER_CLICK = {'pair': {},
                'impair': {}}

# Players log
PLAYER_LOG_SIZE = (1.5*CARD_WIDTH, 0.75*CARD_WIDTH)
PLAYER_LOG_POSITIONS = [(CARD_POSITIONS[0]['pair'][-1][0] + 1.1 * CARD_WIDTH, SCREEN_HEIGHT-PLAYER_LOG_SIZE[1]),
                        (0, CARD_POSITIONS[1]['pair'][-1][1] + 1.1 * CARD_WIDTH),
                        (CARD_POSITIONS[2]['pair'][-1][0] + 1.1 * CARD_WIDTH, 0),
                        (SCREEN_WIDTH-PLAYER_LOG_SIZE[0], CARD_POSITIONS[3]['pair'][0][1] - PLAYER_LOG_SIZE[1]
                         - 0.1 * CARD_WIDTH)]

# Colors
WHITE = (255, 255, 255)
LIGHTGREY = (191, 191, 191)
GREY = (127, 127, 127)
DARKGREY = (63, 63, 63)
BLACK = (0, 0, 0)

# Bidding
CONTRACTS = ('pass', '80', '90', '100', '110', '120', '130', '140', '150', '160', 'Capot', 'Generale')
TRUMPS = ('C', 'D', 'H', 'S', 'AT', 'NT')
VAL = ('Pass', 'Validate', 'Coinche', 'Surcoinche')
# Bidding window: positions, width, height
WIN_POSITION = (SCREEN_WIDTH * 1 / 3, SCREEN_HEIGHT * 1 / 3)
WIN_SIZE = (SCREEN_WIDTH * 1 / 3, SCREEN_HEIGHT * 1 / 3)
# Bidding contracts
BID_WIDTH, BID_HEIGHT = WIN_SIZE[0] * 1 / 8, WIN_SIZE[1] * 1 / 6
BID_X_MARGIN, BID_Y_MARGIN = BID_WIDTH * 2 / 7, BID_HEIGHT * 1 / 3
CONTRACT_BOX = (WIN_POSITION[0], WIN_POSITION[1], WIN_SIZE[0], 2*BID_HEIGHT + 2.5*BID_Y_MARGIN)
CONT_POSITION = ((WIN_POSITION[0] + 1*BID_X_MARGIN + 0*BID_WIDTH, WIN_POSITION[1] + 1*BID_Y_MARGIN + 0*BID_HEIGHT),
                 (WIN_POSITION[0] + 2*BID_X_MARGIN + 1*BID_WIDTH, WIN_POSITION[1] + 1*BID_Y_MARGIN + 0*BID_HEIGHT),
                 (WIN_POSITION[0] + 3*BID_X_MARGIN + 2*BID_WIDTH, WIN_POSITION[1] + 1*BID_Y_MARGIN + 0*BID_HEIGHT),
                 (WIN_POSITION[0] + 4*BID_X_MARGIN + 3*BID_WIDTH, WIN_POSITION[1] + 1*BID_Y_MARGIN + 0*BID_HEIGHT),
                 (WIN_POSITION[0] + 5*BID_X_MARGIN + 4*BID_WIDTH, WIN_POSITION[1] + 1*BID_Y_MARGIN + 0*BID_HEIGHT),
                 (WIN_POSITION[0] + 6*BID_X_MARGIN + 5*BID_WIDTH, WIN_POSITION[1] + 1*BID_Y_MARGIN + 0*BID_HEIGHT),
                 (WIN_POSITION[0] + 1*BID_X_MARGIN + 0*BID_WIDTH, WIN_POSITION[1] + 2*BID_Y_MARGIN + 1*BID_HEIGHT),
                 (WIN_POSITION[0] + 2*BID_X_MARGIN + 1*BID_WIDTH, WIN_POSITION[1] + 2*BID_Y_MARGIN + 1*BID_HEIGHT),
                 (WIN_POSITION[0] + 3*BID_X_MARGIN + 2*BID_WIDTH, WIN_POSITION[1] + 2*BID_Y_MARGIN + 1*BID_HEIGHT),
                 (WIN_POSITION[0] + 4*BID_X_MARGIN + 3*BID_WIDTH, WIN_POSITION[1] + 2*BID_Y_MARGIN + 1*BID_HEIGHT),
                 (WIN_POSITION[0] + 6*BID_X_MARGIN + 4*BID_WIDTH, WIN_POSITION[1] + 2*BID_Y_MARGIN + 1*BID_HEIGHT))
CONT_SIZE = ((BID_WIDTH, BID_HEIGHT), (BID_WIDTH, BID_HEIGHT), (BID_WIDTH, BID_HEIGHT),
             (BID_WIDTH, BID_HEIGHT), (BID_WIDTH, BID_HEIGHT), (BID_WIDTH, BID_HEIGHT),
             (BID_WIDTH, BID_HEIGHT), (BID_WIDTH, BID_HEIGHT), (BID_WIDTH, BID_HEIGHT),
             (BID_WIDTH + BID_X_MARGIN, BID_HEIGHT), (2 * BID_WIDTH, BID_HEIGHT))
# Bidding trumps
TRUMP_BOX = (WIN_POSITION[0], CONTRACT_BOX[1] + CONTRACT_BOX[3], WIN_SIZE[0], BID_HEIGHT + BID_Y_MARGIN)
TRUMP_POSITION = ((WIN_POSITION[0] + 1*BID_X_MARGIN + 0*BID_WIDTH, WIN_POSITION[1] + 3*BID_Y_MARGIN + 2*BID_HEIGHT),
                  (WIN_POSITION[0] + 2*BID_X_MARGIN + 1*BID_WIDTH, WIN_POSITION[1] + 3*BID_Y_MARGIN + 2*BID_HEIGHT),
                  (WIN_POSITION[0] + 3*BID_X_MARGIN + 2*BID_WIDTH, WIN_POSITION[1] + 3*BID_Y_MARGIN + 2*BID_HEIGHT),
                  (WIN_POSITION[0] + 4*BID_X_MARGIN + 3*BID_WIDTH, WIN_POSITION[1] + 3*BID_Y_MARGIN + 2*BID_HEIGHT),
                  (WIN_POSITION[0] + 5*BID_X_MARGIN + 4*BID_WIDTH, WIN_POSITION[1] + 3*BID_Y_MARGIN + 2*BID_HEIGHT),
                  (WIN_POSITION[0] + 6*BID_X_MARGIN + 5*BID_WIDTH, WIN_POSITION[1] + 3*BID_Y_MARGIN + 2*BID_HEIGHT))
TRUMP_SIZE = ((BID_WIDTH, BID_HEIGHT), (BID_WIDTH, BID_HEIGHT), (BID_WIDTH, BID_HEIGHT),
              (BID_WIDTH, BID_HEIGHT), (BID_WIDTH, BID_HEIGHT), (BID_WIDTH, BID_HEIGHT))
# Bidding validation
VAL_BOX = (WIN_POSITION[0], TRUMP_BOX[1] + TRUMP_BOX[3], WIN_SIZE[0], WIN_SIZE[1] - 3*BID_HEIGHT - 3.5*BID_Y_MARGIN)
VAL_WIDTH, VAL_HEIGHT = (WIN_SIZE[0] - 4*BID_X_MARGIN) / 3, VAL_BOX[3] - 1.5*BID_Y_MARGIN
VAL_POSITION = ((WIN_POSITION[0] + 1*BID_X_MARGIN + 0*VAL_WIDTH, VAL_BOX[1] + 0.5*BID_Y_MARGIN),
                (WIN_POSITION[0] + 2*BID_X_MARGIN + 1*VAL_WIDTH, VAL_BOX[1] + 0.5*BID_Y_MARGIN),
                (WIN_POSITION[0] + 3*BID_X_MARGIN + 2*VAL_WIDTH, VAL_BOX[1] + 0.5*BID_Y_MARGIN))
VAL_SIZE = ((VAL_WIDTH, VAL_HEIGHT), (VAL_WIDTH, VAL_HEIGHT), (VAL_WIDTH, VAL_HEIGHT))
