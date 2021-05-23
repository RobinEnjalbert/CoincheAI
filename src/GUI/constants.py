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